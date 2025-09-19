# User Guide

## Overview

AI MCP Server provides a unified interface for AI agents to interact with both Rhino and Grasshopper, enabling sophisticated 3D modeling and parametric design workflows.

## Quick Start

### 1. Installation

```bash
pip install ai-mcp-server
```

### 2. Platform Setup

**Rhino:**
- Install the RhinoMCP plugin from Package Manager
- Run `mcpstart` command in Rhino

**Grasshopper:**
- Install the GH_MCP component
- Add to canvas and enable

### 3. Start Server

```bash
python -m ai_mcp_server.main
```

## Tool Categories

### Unified Tools (Smart Routing)

These tools automatically choose the best platform for the operation:

#### `create_geometry`
Creates geometry with intelligent platform selection.

```python
# Creates a box in Rhino (direct 3D modeling)
create_geometry("box", {"width": 10, "length": 10, "height": 5})

# Creates a parametric pattern in Grasshopper
create_geometry("voronoi", {"points": 50, "radius": 5}, platform="grasshopper")
```

#### `get_document_info`
Gets information from one or both platforms.

```python
# Get info from both platforms
get_document_info()

# Get info from specific platform
get_document_info(platform="rhino")
get_document_info(platform="grasshopper")
```

#### `sync_platforms`
Synchronizes data between platforms.

```python
# Sync Rhino objects to Grasshopper components
sync_platforms("rhino_to_grasshopper")

# Sync Grasshopper components to Rhino objects
sync_platforms("grasshopper_to_rhino")
```

### Rhino Tools

Direct tools for Rhino 3D modeling:

#### `create_rhino_object`
Creates 3D objects in Rhino.

```python
# Create a box
create_rhino_object(
    type="BOX",
    params={"width": 5, "length": 5, "height": 3},
    name="My Box",
    color=[255, 0, 0]  # Red
)

# Create a sphere
create_rhino_object(
    type="SPHERE",
    params={"radius": 2.5},
    translation=[10, 0, 0]
)
```

#### `modify_rhino_object`
Modifies existing objects.

```python
# Move an object
modify_rhino_object(
    object_id="abc123",
    params={"translation": [5, 5, 0]}
)

# Scale an object
modify_rhino_object(
    object_id="abc123", 
    params={"scale": [2, 2, 2]}
)
```

#### `execute_rhino_script`
Executes RhinoScript Python code.

```python
execute_rhino_script("""
import rhinoscriptsyntax as rs
rs.AddPoint([0, 0, 0])
rs.AddCircle([0, 0, 0], 5)
""")
```

### Grasshopper Tools

Tools for parametric design in Grasshopper:

#### `add_grasshopper_component`
Adds components to the canvas.

```python
# Add a number slider
add_grasshopper_component("Number Slider", x=100, y=100)

# Add a circle component
add_grasshopper_component("Circle", x=300, y=100)
```

#### `connect_grasshopper_components`
Connects components together.

```python
# Connect slider to circle radius
connect_grasshopper_components(
    source_id="slider_id",
    target_id="circle_id",
    source_param="Number",
    target_param="Radius"
)
```

#### `create_grasshopper_pattern`
Creates complex patterns from descriptions.

```python
# Create a 3D voronoi pattern
create_grasshopper_pattern("3D voronoi cube with 50 points")

# Create a parametric tower
create_grasshopper_pattern("parametric tower with 10 floors")
```

## Workflow Examples

### Example 1: Basic 3D Modeling

```python
# Create a simple box in Rhino
create_rhino_object(
    type="BOX",
    params={"width": 10, "length": 10, "height": 5},
    name="Base Box"
)

# Get document info
info = get_rhino_document_info()
print(f"Created {len(info['objects'])} objects")
```

### Example 2: Parametric Design

```python
# Create a parametric circle in Grasshopper
add_grasshopper_component("Number Slider", x=100, y=100)  # Radius control
add_grasshopper_component("Circle", x=300, y=100)         # Circle component
add_grasshopper_component("XY Plane", x=300, y=200)      # Base plane

# Connect components
connect_grasshopper_components("slider_id", "circle_id", "Number", "Radius")
connect_grasshopper_components("plane_id", "circle_id", "Plane", "Plane")
```

### Example 3: Hybrid Workflow

```python
# Create geometry in Rhino
create_rhino_object("SPHERE", {"radius": 3}, name="Base Sphere")

# Create parametric version in Grasshopper
create_grasshopper_pattern("parametric sphere with radius control")

# Sync between platforms
sync_platforms("rhino_to_grasshopper")
```

### Example 4: Complex Pattern Creation

```python
# Create a complex parametric pattern
create_grasshopper_pattern("""
Create a 3D voronoi pattern with:
- 100 random points in a 20x20x20 box
- Voronoi cells with boundary surfaces
- Color mapping based on cell volume
- Export to Rhino as brep objects
""")
```

## Best Practices

### 1. Platform Selection

- Use **Rhino** for:
  - Direct 3D modeling
  - Precise geometric operations
  - Script execution
  - File I/O operations

- Use **Grasshopper** for:
  - Parametric design
  - Complex patterns
  - Data-driven geometry
  - Iterative design processes

### 2. Error Handling

Always check connection status before operations:

```python
status = get_server_status()
if not status["connections"]["rhino"]["connected"]:
    print("Rhino not connected!")
```

### 3. Performance Optimization

- Use batch operations when possible
- Limit object counts for large datasets
- Use appropriate timeouts for complex operations

### 4. Data Management

- Use meaningful names for objects
- Organize objects with layers
- Save work frequently
- Use version control for Grasshopper files

## Troubleshooting

### Common Issues

1. **Connection Refused**
   - Verify platforms are running
   - Check port numbers
   - Ensure plugins are installed

2. **Component Not Found**
   - Check component name spelling
   - Verify Grasshopper version compatibility
   - Use search_grasshopper_components()

3. **Invalid Parameters**
   - Check parameter types
   - Use get_component_parameters() for reference
   - Validate connections before creating

### Getting Help

- Check server logs for detailed error messages
- Use get_server_status() to verify connections
- Test with simple operations first
- Consult platform-specific documentation

## Advanced Features

### Custom Patterns

Create custom Grasshopper patterns by extending the pattern library:

```python
# Define custom pattern
custom_pattern = {
    "name": "Custom Tower",
    "description": "Parametric tower with floors",
    "components": [
        {"type": "Number Slider", "x": 100, "y": 100, "id": "floors"},
        {"type": "Number Slider", "x": 100, "y": 150, "id": "height"},
        {"type": "Box", "x": 300, "y": 100, "id": "tower"}
    ],
    "connections": [
        {"source": "floors", "target": "tower", "sourceParam": "Number", "targetParam": "Count"}
    ]
}
```

### Script Integration

Combine RhinoScript with Grasshopper for powerful workflows:

```python
# Create base geometry in Rhino
execute_rhino_script("""
import rhinoscriptsyntax as rs
points = []
for i in range(10):
    for j in range(10):
        points.append([i*2, j*2, 0])
rs.AddPoints(points)
""")

# Create parametric version in Grasshopper
create_grasshopper_pattern("parametric grid with 10x10 points")
```

This guide provides the foundation for using AI MCP Server effectively. For more advanced techniques and examples, see the [API Reference](api-reference.md) and [Examples](examples/).
