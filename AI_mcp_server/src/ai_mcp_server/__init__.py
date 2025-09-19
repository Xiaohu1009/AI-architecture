"""
AI MCP Server - Unified Rhino & Grasshopper Integration

A unified Model Context Protocol (MCP) server that integrates both Rhino and Grasshopper
functionality, providing AI agents with comprehensive 3D modeling and parametric design capabilities.
"""

__version__ = "1.0.0"
__author__ = "AI MCP Server Team"
__email__ = "team@ai-mcp-server.com"

from .core.server import AIServer
from .core.config import Config

__all__ = ["AIServer", "Config"]
