"""
Basic usage examples for AI MCP Server
"""

import asyncio
import json
from ai_mcp_server import AIServer, Config


async def example_rhino_operations():
    """Example Rhino operations"""
    print("=== Rhino Operations Example ===")
    
    # Create server
    config = Config.from_env()
    server = AIServer(config)
    
    # Initialize bridges
    await server.rhino_bridge.initialize()
    
    try:
        # Create a box
        print("Creating a box in Rhino...")
        result = await server.rhino_bridge.create_object(
            "BOX", 
            {"width": 5, "length": 5, "height": 3},
            name="Example Box"
        )
        print(f"Created: {result}")
        
        # Get document info
        print("\nGetting document info...")
        doc_info = await server.rhino_bridge.get_document_info()
        print(f"Document has {len(doc_info.get('objects', []))} objects")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await server.rhino_bridge.cleanup()


async def example_grasshopper_operations():
    """Example Grasshopper operations"""
    print("\n=== Grasshopper Operations Example ===")
    
    # Create server
    config = Config.from_env()
    server = AIServer(config)
    
    # Initialize bridges
    await server.grasshopper_bridge.initialize()
    
    try:
        # Add components
        print("Adding components to Grasshopper...")
        
        # Add a number slider
        slider_result = await server.grasshopper_bridge.add_component("Number Slider", 100, 100)
        print(f"Added slider: {slider_result}")
        
        # Add a circle component
        circle_result = await server.grasshopper_bridge.add_component("Circle", 300, 100)
        print(f"Added circle: {circle_result}")
        
        # Get all components
        print("\nGetting all components...")
        components = await server.grasshopper_bridge.get_all_components()
        print(f"Canvas has {len(components.get('result', []))} components")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await server.grasshopper_bridge.cleanup()


async def example_unified_operations():
    """Example unified operations"""
    print("\n=== Unified Operations Example ===")
    
    # Create server
    config = Config.from_env()
    server = AIServer(config)
    
    # Initialize bridges
    await server.rhino_bridge.initialize()
    await server.grasshopper_bridge.initialize()
    
    try:
        # Get status
        print("Getting server status...")
        status = await server.get_status()
        print(json.dumps(status, indent=2))
        
        # Create geometry with smart routing
        print("\nCreating geometry with smart routing...")
        # This would use the unified tools in a real scenario
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await server.rhino_bridge.cleanup()
        await server.grasshopper_bridge.cleanup()


async def main():
    """Run all examples"""
    print("AI MCP Server Examples")
    print("=" * 50)
    
    # Run examples
    await example_rhino_operations()
    await example_grasshopper_operations()
    await example_unified_operations()
    
    print("\nExamples completed!")


if __name__ == "__main__":
    asyncio.run(main())
