"""
Configuration management for AI MCP Server
"""

import os
from typing import Optional
from pydantic import BaseModel, Field
from pathlib import Path


class RhinoConfig(BaseModel):
    """Rhino connection configuration"""
    host: str = Field(default="127.0.0.1", description="Rhino host address")
    port: int = Field(default=1999, description="Rhino port")
    timeout: float = Field(default=15.0, description="Connection timeout in seconds")
    auto_reconnect: bool = Field(default=True, description="Auto-reconnect on connection loss")


class GrasshopperConfig(BaseModel):
    """Grasshopper connection configuration"""
    host: str = Field(default="127.0.0.1", description="Grasshopper host address")
    port: int = Field(default=8080, description="Grasshopper port")
    timeout: float = Field(default=15.0, description="Connection timeout in seconds")
    auto_reconnect: bool = Field(default=True, description="Auto-reconnect on connection loss")


class ServerConfig(BaseModel):
    """Main server configuration"""
    name: str = Field(default="AI MCP Server", description="Server name")
    version: str = Field(default="1.0.0", description="Server version")
    debug: bool = Field(default=False, description="Enable debug mode")
    log_level: str = Field(default="INFO", description="Logging level")
    max_retries: int = Field(default=3, description="Maximum retry attempts")
    retry_delay: float = Field(default=1.0, description="Delay between retries in seconds")


class Config(BaseModel):
    """Main configuration class"""
    server: ServerConfig = Field(default_factory=ServerConfig)
    rhino: RhinoConfig = Field(default_factory=RhinoConfig)
    grasshopper: GrasshopperConfig = Field(default_factory=GrasshopperConfig)
    
    @classmethod
    def from_env(cls) -> "Config":
        """Create configuration from environment variables"""
        return cls(
            server=ServerConfig(
                name=os.getenv("AI_MCP_SERVER_NAME", "AI MCP Server"),
                debug=os.getenv("AI_MCP_DEBUG", "false").lower() == "true",
                log_level=os.getenv("AI_MCP_LOG_LEVEL", "INFO"),
            ),
            rhino=RhinoConfig(
                host=os.getenv("RHINO_HOST", "127.0.0.1"),
                port=int(os.getenv("RHINO_PORT", "1999")),
                timeout=float(os.getenv("RHINO_TIMEOUT", "15.0")),
            ),
            grasshopper=GrasshopperConfig(
                host=os.getenv("GRASSHOPPER_HOST", "127.0.0.1"),
                port=int(os.getenv("GRASSHOPPER_PORT", "8080")),
                timeout=float(os.getenv("GRASSHOPPER_TIMEOUT", "15.0")),
            ),
        )
    
    @classmethod
    def from_file(cls, config_path: Path) -> "Config":
        """Create configuration from file"""
        import json
        
        if not config_path.exists():
            raise FileNotFoundError(f"Configuration file not found: {config_path}")
        
        with open(config_path, 'r') as f:
            data = json.load(f)
        
        return cls(**data)
    
    def save_to_file(self, config_path: Path) -> None:
        """Save configuration to file"""
        import json
        
        config_path.parent.mkdir(parents=True, exist_ok=True)
        with open(config_path, 'w') as f:
            json.dump(self.model_dump(), f, indent=2)
