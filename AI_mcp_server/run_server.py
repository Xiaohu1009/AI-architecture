#!/usr/bin/env python3
"""
AI MCP Server Runner
"""

import asyncio
import sys
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from ai_mcp_server.core.config import Config
from ai_mcp_server.core.server import AIServer


def main():
    """Main entry point"""
    try:
        # Load configuration
        config = Config.from_env()
        
        # Create and run server
        server = AIServer(config)
        server.run()
        
    except KeyboardInterrupt:
        print("\nServer stopped by user")
    except Exception as e:
        print(f"Server error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
