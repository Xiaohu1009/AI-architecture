"""
Main entry point for AI MCP Server
"""

import asyncio
import sys
from pathlib import Path
from typing import Optional

from .core.config import Config
from .core.server import AIServer


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
        sys.exit(0)
    except Exception as e:
        print(f"Server error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
