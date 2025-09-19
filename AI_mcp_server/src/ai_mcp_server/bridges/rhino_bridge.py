"""
Rhino bridge implementation
"""

import logging
from typing import Dict, Any
from .base_bridge import BaseBridge, ConnectionConfig


class RhinoBridge(BaseBridge):
    """Bridge to Rhino platform"""
    
    def __init__(self, config: ConnectionConfig, logger: logging.Logger):
        super().__init__(config, logger)
    
    async def ping(self) -> Dict[str, Any]:
        """Ping Rhino to check connection"""
        try:
            return await self.send_command("ping", {})
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    async def create_object(self, object_type: str, params: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        """Create object in Rhino"""
        command_params = {
            "type": object_type,
            "params": params
        }
        
        # Add optional parameters
        for key, value in kwargs.items():
            if value is not None:
                command_params[key] = value
        
        return await self.send_command("create_object", command_params)
    
    async def get_document_info(self) -> Dict[str, Any]:
        """Get Rhino document information"""
        return await self.send_command("get_document_info", {})
    
    async def get_object_info(self, object_id: str) -> Dict[str, Any]:
        """Get object information"""
        return await self.send_command("get_object_info", {"object_id": object_id})
    
    async def modify_object(self, object_id: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Modify object in Rhino"""
        return await self.send_command("modify_object", {
            "object_id": object_id,
            "params": params
        })
    
    async def delete_object(self, object_id: str) -> Dict[str, Any]:
        """Delete object in Rhino"""
        return await self.send_command("delete_object", {"object_id": object_id})
    
    async def select_objects(self, filters: Dict[str, Any]) -> Dict[str, Any]:
        """Select objects based on filters"""
        return await self.send_command("select_objects", {"filters": filters})
    
    async def execute_script(self, script: str) -> Dict[str, Any]:
        """Execute RhinoScript Python code"""
        return await self.send_command("execute_rhinoscript_python_code", {"script": script})
    
    async def create_layer(self, name: str, color: list = None) -> Dict[str, Any]:
        """Create layer in Rhino"""
        params = {"name": name}
        if color:
            params["color"] = color
        return await self.send_command("create_layer", params)
    
    async def get_current_layer(self) -> Dict[str, Any]:
        """Get current layer information"""
        return await self.send_command("get_or_set_current_layer", {})
    
    async def set_current_layer(self, layer_name: str) -> Dict[str, Any]:
        """Set current layer"""
        return await self.send_command("get_or_set_current_layer", {"layer_name": layer_name})
