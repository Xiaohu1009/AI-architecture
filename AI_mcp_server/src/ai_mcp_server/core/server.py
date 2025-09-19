"""
Main AI MCP Server implementation
"""

import asyncio
import logging
from typing import Dict, Any, Optional
from contextlib import asynccontextmanager

from mcp.server.fastmcp import FastMCP, Context
from .config import Config
from ..bridges.rhino_bridge import RhinoBridge
from ..bridges.grasshopper_bridge import GrasshopperBridge
from ..tools.unified_tools import register_unified_tools
from ..tools.rhino_tools import register_rhino_tools
from ..tools.grasshopper_tools import register_grasshopper_tools


class AIServer:
    """Main AI MCP Server class"""
    
    def __init__(self, config: Optional[Config] = None):
        self.config = config or Config.from_env()
        self.logger = self._setup_logging()
        
        # Initialize bridges
        self.rhino_bridge = RhinoBridge(self.config.rhino, self.logger)
        self.grasshopper_bridge = GrasshopperBridge(self.config.grasshopper, self.logger)
        
        # Initialize MCP server
        self.mcp_server = FastMCP(
            self.config.server.name,
            lifespan=self._server_lifespan
        )
        
        # Register tools
        self._register_tools()
        
        self.logger.info(f"AI MCP Server initialized: {self.config.server.name} v{self.config.server.version}")
    
    def _setup_logging(self) -> logging.Logger:
        """Setup logging configuration"""
        logging.basicConfig(
            level=getattr(logging, self.config.server.log_level),
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        return logging.getLogger("AIServer")
    
    def _register_tools(self) -> None:
        """Register all MCP tools"""
        # Register unified tools (smart routing)
        register_unified_tools(self.mcp_server, self.rhino_bridge, self.grasshopper_bridge)
        
        # Register platform-specific tools
        register_rhino_tools(self.mcp_server, self.rhino_bridge)
        register_grasshopper_tools(self.mcp_server, self.grasshopper_bridge)
        
        self.logger.info("All MCP tools registered")
    
    @asynccontextmanager
    async def _server_lifespan(self, server: FastMCP) -> Dict[str, Any]:
        """Manage server startup and shutdown lifecycle"""
        try:
            self.logger.info("Starting AI MCP Server...")
            
            # Initialize bridges
            await self.rhino_bridge.initialize()
            await self.grasshopper_bridge.initialize()
            
            # Check connections
            rhino_status = await self.rhino_bridge.check_connection()
            grasshopper_status = await self.grasshopper_bridge.check_connection()
            
            self.logger.info(f"Rhino connection: {'Connected' if rhino_status else 'Disconnected'}")
            self.logger.info(f"Grasshopper connection: {'Connected' if grasshopper_status else 'Disconnected'}")
            
            if not rhino_status and not grasshopper_status:
                self.logger.warning("Neither Rhino nor Grasshopper is connected. Some tools may not work.")
            
            yield {}
            
        except Exception as e:
            self.logger.error(f"Error during server startup: {e}")
            raise
        finally:
            self.logger.info("Shutting down AI MCP Server...")
            await self.rhino_bridge.cleanup()
            await self.grasshopper_bridge.cleanup()
            self.logger.info("AI MCP Server shutdown complete")
    
    def start(self) -> None:
        """Start the MCP server"""
        try:
            self.logger.info("Starting MCP server...")
            # Use stdio transport for MCP
            self.mcp_server.run(transport="stdio")
        except Exception as e:
            self.logger.error(f"Error starting MCP server: {e}")
            raise
    
    def run(self) -> None:
        """Run the server (blocking)"""
        try:
            self.start()
        except KeyboardInterrupt:
            self.logger.info("Server stopped by user")
        except Exception as e:
            self.logger.error(f"Server error: {e}")
            raise
    
    async def get_status(self) -> Dict[str, Any]:
        """Get server status"""
        rhino_status = await self.rhino_bridge.check_connection()
        grasshopper_status = await self.grasshopper_bridge.check_connection()
        
        return {
            "server": {
                "name": self.config.server.name,
                "version": self.config.server.version,
                "status": "running"
            },
            "connections": {
                "rhino": {
                    "connected": rhino_status,
                    "host": self.config.rhino.host,
                    "port": self.config.rhino.port
                },
                "grasshopper": {
                    "connected": grasshopper_status,
                    "host": self.config.grasshopper.host,
                    "port": self.config.grasshopper.port
                }
            }
        }
