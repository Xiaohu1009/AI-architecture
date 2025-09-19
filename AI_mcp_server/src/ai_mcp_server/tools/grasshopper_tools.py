"""
Grasshopper-specific MCP tools
"""

from typing import Dict, Any, List, Optional
from mcp.server.fastmcp import FastMCP, Context
from ..bridges.grasshopper_bridge import GrasshopperBridge


def register_grasshopper_tools(server: FastMCP, grasshopper_bridge: GrasshopperBridge):
    """Register Grasshopper-specific tools"""
    
    @server.tool()
    async def add_grasshopper_component(
        ctx: Context,
        component_type: str,
        x: float = 100.0,
        y: float = 100.0
    ) -> str:
        """
        Add a component to the Grasshopper canvas
        
        Args:
            component_type: Component type (point, curve, circle, line, panel, slider, etc.)
            x: X coordinate on the canvas
            y: Y coordinate on the canvas
        
        Returns:
            Result of adding the component
        """
        try:
            result = await grasshopper_bridge.add_component(component_type, x, y)
            return f"Added {component_type} component: {result.get('id', 'Unknown')}"
        except Exception as e:
            return f"Error adding component: {str(e)}"
    
    @server.tool()
    async def connect_grasshopper_components(
        ctx: Context,
        source_id: str,
        target_id: str,
        source_param: Optional[str] = None,
        target_param: Optional[str] = None,
        source_param_index: Optional[int] = None,
        target_param_index: Optional[int] = None
    ) -> str:
        """
        Connect two components in the Grasshopper canvas
        
        Args:
            source_id: ID of the source component (output)
            target_id: ID of the target component (input)
            source_param: Name of the source parameter (optional)
            target_param: Name of the target parameter (optional)
            source_param_index: Index of the source parameter (optional)
            target_param_index: Index of the target parameter (optional)
        
        Returns:
            Result of connecting the components
        """
        try:
            result = await grasshopper_bridge.connect_components(
                source_id, target_id, source_param, target_param,
                source_param_index, target_param_index
            )
            return f"Connected components: {result.get('message', 'Success')}"
        except Exception as e:
            return f"Error connecting components: {str(e)}"
    
    @server.tool()
    async def get_grasshopper_document_info(ctx: Context) -> str:
        """Get information about the Grasshopper document"""
        try:
            result = await grasshopper_bridge.get_document_info()
            import json
            return json.dumps(result, indent=2)
        except Exception as e:
            return f"Error getting document info: {str(e)}"
    
    @server.tool()
    async def get_grasshopper_components(ctx: Context) -> str:
        """Get a list of all components in the current document"""
        try:
            result = await grasshopper_bridge.get_all_components()
            import json
            return json.dumps(result, indent=2)
        except Exception as e:
            return f"Error getting components: {str(e)}"
    
    @server.tool()
    async def get_grasshopper_component_info(ctx: Context, component_id: str) -> str:
        """Get detailed information about a specific component"""
        try:
            result = await grasshopper_bridge.get_component_info(component_id)
            import json
            return json.dumps(result, indent=2)
        except Exception as e:
            return f"Error getting component info: {str(e)}"
    
    @server.tool()
    async def get_grasshopper_connections(ctx: Context) -> str:
        """Get a list of all connections between components"""
        try:
            result = await grasshopper_bridge.get_connections()
            import json
            return json.dumps(result, indent=2)
        except Exception as e:
            return f"Error getting connections: {str(e)}"
    
    @server.tool()
    async def create_grasshopper_pattern(ctx: Context, description: str) -> str:
        """
        Create a pattern of components based on a high-level description
        
        Args:
            description: High-level description of what to create (e.g., '3D voronoi cube')
        
        Returns:
            Result of creating the pattern
        """
        try:
            result = await grasshopper_bridge.create_pattern(description)
            return f"Created pattern: {result.get('message', 'Success')}"
        except Exception as e:
            return f"Error creating pattern: {str(e)}"
    
    @server.tool()
    async def get_grasshopper_available_patterns(ctx: Context, query: str) -> str:
        """
        Get a list of available patterns that match a query
        
        Args:
            query: Query to search for patterns
        
        Returns:
            List of available patterns
        """
        try:
            result = await grasshopper_bridge.get_available_patterns(query)
            import json
            return json.dumps(result, indent=2)
        except Exception as e:
            return f"Error getting patterns: {str(e)}"
    
    @server.tool()
    async def search_grasshopper_components(ctx: Context, query: str) -> str:
        """
        Search for components by name or category
        
        Args:
            query: Search query
        
        Returns:
            List of components matching the search query
        """
        try:
            result = await grasshopper_bridge.search_components(query)
            import json
            return json.dumps(result, indent=2)
        except Exception as e:
            return f"Error searching components: {str(e)}"
    
    @server.tool()
    async def get_grasshopper_component_parameters(ctx: Context, component_type: str) -> str:
        """
        Get a list of parameters for a specific component type
        
        Args:
            component_type: Type of component to get parameters for
        
        Returns:
            List of input and output parameters for the component type
        """
        try:
            result = await grasshopper_bridge.get_component_parameters(component_type)
            import json
            return json.dumps(result, indent=2)
        except Exception as e:
            return f"Error getting component parameters: {str(e)}"
    
    @server.tool()
    async def validate_grasshopper_connection(
        ctx: Context,
        source_id: str,
        target_id: str,
        source_param: Optional[str] = None,
        target_param: Optional[str] = None
    ) -> str:
        """
        Validate if a connection between two components is possible
        
        Args:
            source_id: ID of the source component (output)
            target_id: ID of the target component (input)
            source_param: Name of the source parameter (optional)
            target_param: Name of the target parameter (optional)
        
        Returns:
            Whether the connection is valid and any potential issues
        """
        try:
            result = await grasshopper_bridge.validate_connection(
                source_id, target_id, source_param, target_param
            )
            import json
            return json.dumps(result, indent=2)
        except Exception as e:
            return f"Error validating connection: {str(e)}"
    
    @server.tool()
    async def clear_grasshopper_document(ctx: Context) -> str:
        """Clear the Grasshopper document"""
        try:
            result = await grasshopper_bridge.clear_document()
            return f"Cleared document: {result.get('message', 'Success')}"
        except Exception as e:
            return f"Error clearing document: {str(e)}"
    
    @server.tool()
    async def save_grasshopper_document(ctx: Context, path: str) -> str:
        """Save the Grasshopper document"""
        try:
            result = await grasshopper_bridge.save_document(path)
            return f"Saved document to {path}: {result.get('message', 'Success')}"
        except Exception as e:
            return f"Error saving document: {str(e)}"
    
    @server.tool()
    async def load_grasshopper_document(ctx: Context, path: str) -> str:
        """Load a Grasshopper document"""
        try:
            result = await grasshopper_bridge.load_document(path)
            return f"Loaded document from {path}: {result.get('message', 'Success')}"
        except Exception as e:
            return f"Error loading document: {str(e)}"
