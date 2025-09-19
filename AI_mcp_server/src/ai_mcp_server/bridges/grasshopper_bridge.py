"""
Grasshopper bridge implementation
"""

import logging
from typing import Dict, Any, List, Optional
from .base_bridge import BaseBridge, ConnectionConfig


class GrasshopperBridge(BaseBridge):
    """Bridge to Grasshopper platform"""
    
    def __init__(self, config: ConnectionConfig, logger: logging.Logger):
        super().__init__(config, logger)
    
    async def ping(self) -> Dict[str, Any]:
        """Ping Grasshopper to check connection"""
        try:
            return await self.send_command("ping", {})
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    async def add_component(self, component_type: str, x: float, y: float) -> Dict[str, Any]:
        """Add component to Grasshopper canvas"""
        return await self.send_command("add_component", {
            "type": component_type,
            "x": x,
            "y": y
        })
    
    async def connect_components(self, source_id: str, target_id: str, 
                                source_param: Optional[str] = None, 
                                target_param: Optional[str] = None,
                                source_param_index: Optional[int] = None,
                                target_param_index: Optional[int] = None) -> Dict[str, Any]:
        """Connect two components"""
        params = {
            "sourceId": source_id,
            "targetId": target_id
        }
        
        if source_param:
            params["sourceParam"] = source_param
        elif source_param_index is not None:
            params["sourceParamIndex"] = source_param_index
            
        if target_param:
            params["targetParam"] = target_param
        elif target_param_index is not None:
            params["targetParamIndex"] = target_param_index
        
        return await self.send_command("connect_components", params)
    
    async def get_document_info(self) -> Dict[str, Any]:
        """Get Grasshopper document information"""
        return await self.send_command("get_document_info", {})
    
    async def get_all_components(self) -> Dict[str, Any]:
        """Get all components in the document"""
        return await self.send_command("get_all_components", {})
    
    async def get_component_info(self, component_id: str) -> Dict[str, Any]:
        """Get component information"""
        return await self.send_command("get_component_info", {"componentId": component_id})
    
    async def get_connections(self) -> Dict[str, Any]:
        """Get all connections between components"""
        return await self.send_command("get_connections", {})
    
    async def create_pattern(self, description: str) -> Dict[str, Any]:
        """Create pattern based on description"""
        return await self.send_command("create_pattern", {"description": description})
    
    async def get_available_patterns(self, query: str) -> Dict[str, Any]:
        """Get available patterns matching query"""
        return await self.send_command("get_available_patterns", {"query": query})
    
    async def search_components(self, query: str) -> Dict[str, Any]:
        """Search for components by name or category"""
        return await self.send_command("search_components", {"query": query})
    
    async def get_component_parameters(self, component_type: str) -> Dict[str, Any]:
        """Get parameters for a component type"""
        return await self.send_command("get_component_parameters", {"componentType": component_type})
    
    async def validate_connection(self, source_id: str, target_id: str,
                                source_param: Optional[str] = None,
                                target_param: Optional[str] = None) -> Dict[str, Any]:
        """Validate if connection is possible"""
        params = {
            "sourceId": source_id,
            "targetId": target_id
        }
        
        if source_param:
            params["sourceParam"] = source_param
        if target_param:
            params["targetParam"] = target_param
        
        return await self.send_command("validate_connection", params)
    
    async def clear_document(self) -> Dict[str, Any]:
        """Clear the Grasshopper document"""
        return await self.send_command("clear_document", {})
    
    async def save_document(self, path: str) -> Dict[str, Any]:
        """Save the Grasshopper document"""
        return await self.send_command("save_document", {"path": path})
    
    async def load_document(self, path: str) -> Dict[str, Any]:
        """Load a Grasshopper document"""
        return await self.send_command("load_document", {"path": path})
