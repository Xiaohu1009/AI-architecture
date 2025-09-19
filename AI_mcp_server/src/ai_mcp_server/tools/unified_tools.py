"""
Unified tools that provide smart routing between Rhino and Grasshopper
"""

from typing import Dict, Any, List, Optional
from mcp.server.fastmcp import FastMCP, Context
from ..bridges.rhino_bridge import RhinoBridge
from ..bridges.grasshopper_bridge import GrasshopperBridge


def register_unified_tools(server: FastMCP, rhino_bridge: RhinoBridge, grasshopper_bridge: GrasshopperBridge):
    """Register unified tools with smart routing"""
    
    @server.tool()
    async def create_geometry(
        ctx: Context,
        geometry_type: str,
        params: Dict[str, Any],
        platform: Optional[str] = None,
        **kwargs
    ) -> str:
        """
        Create geometry with smart platform routing
        
        Args:
            geometry_type: Type of geometry to create (box, sphere, circle, etc.)
            params: Geometry parameters
            platform: Target platform ('rhino', 'grasshopper', or None for auto)
            **kwargs: Additional parameters (name, color, translation, etc.)
        
        Returns:
            Result message
        """
        # Auto-detect platform if not specified
        if platform is None:
            platform = _detect_platform(geometry_type, params)
        
        if platform == "rhino":
            result = await rhino_bridge.create_object(geometry_type, params, **kwargs)
            return f"Created {geometry_type} in Rhino: {result.get('name', 'Unknown')}"
        elif platform == "grasshopper":
            # For Grasshopper, we need to create a pattern or individual components
            if geometry_type in ["box", "sphere", "cylinder", "cone"]:
                pattern_desc = f"Create a {geometry_type} with parameters: {params}"
                result = await grasshopper_bridge.create_pattern(pattern_desc)
                return f"Created {geometry_type} pattern in Grasshopper: {result.get('message', 'Success')}"
            else:
                # Create individual components
                component_type = _map_geometry_to_component(geometry_type)
                result = await grasshopper_bridge.add_component(component_type, 100, 100)
                return f"Added {component_type} component in Grasshopper: {result.get('id', 'Unknown')}"
        else:
            raise ValueError(f"Unknown platform: {platform}")
    
    @server.tool()
    async def get_document_info(ctx: Context, platform: Optional[str] = None) -> str:
        """
        Get document information from specified platform or both
        
        Args:
            platform: Target platform ('rhino', 'grasshopper', or None for both)
        
        Returns:
            Document information as JSON string
        """
        import json
        
        if platform == "rhino":
            result = await rhino_bridge.get_document_info()
            return json.dumps({"rhino": result}, indent=2)
        elif platform == "grasshopper":
            result = await grasshopper_bridge.get_document_info()
            return json.dumps({"grasshopper": result}, indent=2)
        else:
            # Get from both platforms
            rhino_info = await rhino_bridge.get_document_info()
            grasshopper_info = await grasshopper_bridge.get_document_info()
            
            return json.dumps({
                "rhino": rhino_info,
                "grasshopper": grasshopper_info
            }, indent=2)
    
    @server.tool()
    async def sync_platforms(ctx: Context, direction: str = "rhino_to_grasshopper") -> str:
        """
        Synchronize data between platforms
        
        Args:
            direction: Sync direction ('rhino_to_grasshopper' or 'grasshopper_to_rhino')
        
        Returns:
            Sync result message
        """
        if direction == "rhino_to_grasshopper":
            # Get objects from Rhino and create corresponding Grasshopper components
            rhino_info = await rhino_bridge.get_document_info()
            objects = rhino_info.get("objects", [])
            
            synced_count = 0
            for obj in objects[:5]:  # Limit to first 5 objects
                obj_type = obj.get("type", "").lower()
                component_type = _map_geometry_to_component(obj_type)
                if component_type:
                    await grasshopper_bridge.add_component(component_type, 100 + synced_count * 150, 100)
                    synced_count += 1
            
            return f"Synced {synced_count} objects from Rhino to Grasshopper"
        
        elif direction == "grasshopper_to_rhino":
            # Get components from Grasshopper and create corresponding Rhino objects
            grasshopper_info = await grasshopper_bridge.get_all_components()
            components = grasshopper_info.get("result", [])
            
            synced_count = 0
            for comp in components[:5]:  # Limit to first 5 components
                comp_type = comp.get("type", "").lower()
                geometry_type = _map_component_to_geometry(comp_type)
                if geometry_type:
                    # Create basic geometry with default parameters
                    params = _get_default_params(geometry_type)
                    await rhino_bridge.create_object(geometry_type, params)
                    synced_count += 1
            
            return f"Synced {synced_count} components from Grasshopper to Rhino"
        
        else:
            raise ValueError(f"Unknown sync direction: {direction}")
    
    @server.tool()
    async def get_server_status(ctx: Context) -> str:
        """
        Get server and platform connection status
        
        Returns:
            Status information as JSON string
        """
        import json
        
        rhino_status = await rhino_bridge.check_connection()
        grasshopper_status = await grasshopper_bridge.check_connection()
        
        status = {
            "server": "AI MCP Server",
            "version": "1.0.0",
            "connections": {
                "rhino": {
                    "connected": rhino_status,
                    "host": rhino_bridge.config.host,
                    "port": rhino_bridge.config.port
                },
                "grasshopper": {
                    "connected": grasshopper_status,
                    "host": grasshopper_bridge.config.host,
                    "port": grasshopper_bridge.config.port
                }
            }
        }
        
        return json.dumps(status, indent=2)


def _detect_platform(geometry_type: str, params: Dict[str, Any]) -> str:
    """Detect the best platform for creating geometry"""
    # Simple heuristics for platform selection
    if geometry_type in ["box", "sphere", "cylinder", "cone", "point", "line", "circle"]:
        # These are better suited for direct Rhino creation
        return "rhino"
    elif geometry_type in ["voronoi", "pattern", "parametric"]:
        # These are better suited for Grasshopper
        return "grasshopper"
    else:
        # Default to Rhino
        return "rhino"


def _map_geometry_to_component(geometry_type: str) -> Optional[str]:
    """Map geometry type to Grasshopper component type"""
    mapping = {
        "box": "Box",
        "sphere": "Sphere", 
        "cylinder": "Cylinder",
        "cone": "Cone",
        "circle": "Circle",
        "line": "Line",
        "point": "Point",
        "plane": "XY Plane"
    }
    return mapping.get(geometry_type.lower())


def _map_component_to_geometry(component_type: str) -> Optional[str]:
    """Map Grasshopper component type to geometry type"""
    mapping = {
        "box": "BOX",
        "sphere": "SPHERE",
        "cylinder": "CYLINDER", 
        "cone": "CONE",
        "circle": "CIRCLE",
        "line": "LINE",
        "point": "POINT"
    }
    return mapping.get(component_type.lower())


def _get_default_params(geometry_type: str) -> Dict[str, Any]:
    """Get default parameters for geometry type"""
    defaults = {
        "BOX": {"width": 1.0, "length": 1.0, "height": 1.0},
        "SPHERE": {"radius": 1.0},
        "CYLINDER": {"radius": 1.0, "height": 2.0},
        "CONE": {"radius": 1.0, "height": 2.0},
        "CIRCLE": {"center": [0, 0, 0], "radius": 1.0},
        "LINE": {"start": [0, 0, 0], "end": [1, 1, 1]},
        "POINT": {"x": 0, "y": 0, "z": 0}
    }
    return defaults.get(geometry_type, {})
