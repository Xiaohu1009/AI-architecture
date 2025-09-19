"""
Rhino-specific MCP tools
"""

from typing import Dict, Any, List, Optional
from mcp.server.fastmcp import FastMCP, Context
from ..bridges.rhino_bridge import RhinoBridge


def register_rhino_tools(server: FastMCP, rhino_bridge: RhinoBridge):
    """Register Rhino-specific tools"""
    
    @server.tool()
    async def create_rhino_object(
        ctx: Context,
        type: str = "BOX",
        name: Optional[str] = None,
        color: Optional[List[int]] = None,
        params: Dict[str, Any] = {},
        translation: Optional[List[float]] = None,
        rotation: Optional[List[float]] = None,
        scale: Optional[List[float]] = None,
    ) -> str:
        """
        Create a new object in the Rhino document.
        
        Parameters:
        - type: Object type ("POINT", "LINE", "POLYLINE", "CIRCLE", "ARC", "ELLIPSE", "CURVE", "BOX", "SPHERE", "CONE", "CYLINDER", "PIPE", "SURFACE")
        - name: Optional name for the object
        - color: Optional [r, g, b] color values (0-255) for the object
        - params: Type-specific parameters dictionary
        - translation: Optional [x, y, z] translation vector
        - rotation: Optional [x, y, z] rotation in radians
        - scale: Optional [x, y, z] scale factors
        
        Returns:
        A message indicating the created object name.
        """
        try:
            result = await rhino_bridge.create_object(
                type, params, name=name, color=color,
                translation=translation, rotation=rotation, scale=scale
            )
            return f"Created {type} object: {result.get('name', 'Unknown')}"
        except Exception as e:
            return f"Error creating object: {str(e)}"
    
    @server.tool()
    async def get_rhino_document_info(ctx: Context) -> str:
        """Get detailed information about the current Rhino document"""
        try:
            result = await rhino_bridge.get_document_info()
            import json
            return json.dumps(result, indent=2)
        except Exception as e:
            return f"Error getting document info: {str(e)}"
    
    @server.tool()
    async def get_rhino_object_info(ctx: Context, object_id: str) -> str:
        """Get information about a specific Rhino object"""
        try:
            result = await rhino_bridge.get_object_info(object_id)
            import json
            return json.dumps(result, indent=2)
        except Exception as e:
            return f"Error getting object info: {str(e)}"
    
    @server.tool()
    async def modify_rhino_object(ctx: Context, object_id: str, params: Dict[str, Any]) -> str:
        """Modify a Rhino object"""
        try:
            result = await rhino_bridge.modify_object(object_id, params)
            return f"Modified object {object_id}: {result.get('message', 'Success')}"
        except Exception as e:
            return f"Error modifying object: {str(e)}"
    
    @server.tool()
    async def delete_rhino_object(ctx: Context, object_id: str) -> str:
        """Delete a Rhino object"""
        try:
            result = await rhino_bridge.delete_object(object_id)
            return f"Deleted object {object_id}: {result.get('message', 'Success')}"
        except Exception as e:
            return f"Error deleting object: {str(e)}"
    
    @server.tool()
    async def select_rhino_objects(ctx: Context, filters: Dict[str, Any]) -> str:
        """Select objects in Rhino based on filters"""
        try:
            result = await rhino_bridge.select_objects(filters)
            return f"Selected objects: {result.get('count', 0)} objects"
        except Exception as e:
            return f"Error selecting objects: {str(e)}"
    
    @server.tool()
    async def execute_rhino_script(ctx: Context, script: str) -> str:
        """Execute RhinoScript Python code in Rhino"""
        try:
            result = await rhino_bridge.execute_script(script)
            return f"Script executed: {result.get('message', 'Success')}"
        except Exception as e:
            return f"Error executing script: {str(e)}"
    
    @server.tool()
    async def create_rhino_layer(ctx: Context, name: str, color: Optional[List[int]] = None) -> str:
        """Create a new layer in Rhino"""
        try:
            result = await rhino_bridge.create_layer(name, color)
            return f"Created layer '{name}': {result.get('message', 'Success')}"
        except Exception as e:
            return f"Error creating layer: {str(e)}"
    
    @server.tool()
    async def get_rhino_current_layer(ctx: Context) -> str:
        """Get current layer information in Rhino"""
        try:
            result = await rhino_bridge.get_current_layer()
            import json
            return json.dumps(result, indent=2)
        except Exception as e:
            return f"Error getting current layer: {str(e)}"
    
    @server.tool()
    async def set_rhino_current_layer(ctx: Context, layer_name: str) -> str:
        """Set current layer in Rhino"""
        try:
            result = await rhino_bridge.set_current_layer(layer_name)
            return f"Set current layer to '{layer_name}': {result.get('message', 'Success')}"
        except Exception as e:
            return f"Error setting current layer: {str(e)}"
    
    @server.tool()
    async def create_rhino_objects(ctx: Context, objects: List[Dict[str, Any]]) -> str:
        """Create multiple objects in Rhino"""
        try:
            created_count = 0
            errors = []
            
            for obj_data in objects:
                try:
                    obj_type = obj_data.get("type", "BOX")
                    params = obj_data.get("params", {})
                    name = obj_data.get("name")
                    color = obj_data.get("color")
                    
                    await rhino_bridge.create_object(obj_type, params, name=name, color=color)
                    created_count += 1
                except Exception as e:
                    errors.append(f"Object {obj_data}: {str(e)}")
            
            result_msg = f"Created {created_count} objects"
            if errors:
                result_msg += f". Errors: {'; '.join(errors)}"
            
            return result_msg
        except Exception as e:
            return f"Error creating objects: {str(e)}"
