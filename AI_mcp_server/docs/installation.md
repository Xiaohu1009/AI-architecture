# Installation Guide

## Prerequisites

Before installing AI MCP Server, ensure you have the following:

### System Requirements
- **Python 3.10+** (recommended: Python 3.11 or 3.12)
- **Rhino 7+** (Windows or Mac)
- **Grasshopper** (installed with Rhino)
- **uv package manager** (recommended) or pip

### Platform-Specific Requirements

#### Windows
- Windows 10 or later
- Visual Studio Build Tools (for compiling C# components)

#### macOS
- macOS 10.15 or later
- Xcode Command Line Tools

## Installation Methods

### Method 1: Using uv (Recommended)

1. **Install uv** (if not already installed):
   ```bash
   # Windows
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   
   # macOS
   brew install uv
   
   # Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Install AI MCP Server**:
   ```bash
   uv add ai-mcp-server
   ```

### Method 2: Using pip

1. **Install from PyPI**:
   ```bash
   pip install ai-mcp-server
   ```

2. **Install from source**:
   ```bash
   git clone https://github.com/your-org/ai-mcp-server.git
   cd ai-mcp-server
   pip install -e .
   ```

### Method 3: Development Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-org/ai-mcp-server.git
   cd ai-mcp-server
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -e ".[dev]"
   ```

## Platform Setup

### Rhino Setup

1. **Install Rhino Plugin**:
   - Open Rhino
   - Go to Tools > Package Manager
   - Search for `rhinomcp`
   - Click Install

2. **Start Rhino MCP Server**:
   - In Rhino, type `mcpstart` in the command line
   - Verify the server is running on port 1999

### Grasshopper Setup

1. **Install Grasshopper MCP Component**:
   - Download `GH_MCP.gha` from the releases
   - Copy to `%APPDATA%\Grasshopper\Libraries\` (Windows) or `~/Library/Application Support/Grasshopper/Libraries/` (Mac)
   - Restart Rhino and Grasshopper

2. **Add Component to Canvas**:
   - Open Grasshopper
   - Find the GH_MCP component in the component panel
   - Add it to your canvas
   - Enable the component (set the Enabled input to True)

## Configuration

### Environment Variables

Create a `.env` file or set environment variables:

```bash
# Server Configuration
AI_MCP_SERVER_NAME="AI MCP Server"
AI_MCP_DEBUG=false
AI_MCP_LOG_LEVEL=INFO

# Rhino Configuration
RHINO_HOST=127.0.0.1
RHINO_PORT=1999
RHINO_TIMEOUT=15.0

# Grasshopper Configuration
GRASSHOPPER_HOST=127.0.0.1
GRASSHOPPER_PORT=8080
GRASSHOPPER_TIMEOUT=15.0
```

### Configuration File

Create `config.json`:

```json
{
  "server": {
    "name": "AI MCP Server",
    "version": "1.0.0",
    "debug": false,
    "log_level": "INFO"
  },
  "rhino": {
    "host": "127.0.0.1",
    "port": 1999,
    "timeout": 15.0,
    "auto_reconnect": true
  },
  "grasshopper": {
    "host": "127.0.0.1",
    "port": 8080,
    "timeout": 15.0,
    "auto_reconnect": true
  }
}
```

## AI Client Configuration

### Claude Desktop

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "ai_mcp": {
      "command": "python",
      "args": ["-m", "ai_mcp_server.main"]
    }
  }
}
```

### Cursor

Create `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "ai_mcp": {
      "command": "python",
      "args": ["-m", "ai_mcp_server.main"]
    }
  }
}
```

## Verification

### Test Installation

1. **Start the server**:
   ```bash
   python -m ai_mcp_server.main
   ```

2. **Check connections**:
   - Ensure Rhino is running with MCP plugin active
   - Ensure Grasshopper is open with GH_MCP component enabled
   - Verify both connections show as "Connected"

3. **Run examples**:
   ```bash
   python examples/basic_usage.py
   ```

### Troubleshooting

#### Common Issues

1. **Connection Refused**:
   - Verify Rhino/Grasshopper are running
   - Check port numbers (1999 for Rhino, 8080 for Grasshopper)
   - Ensure plugins are properly installed

2. **Import Errors**:
   - Verify Python version (3.10+)
   - Check all dependencies are installed
   - Try reinstalling the package

3. **Permission Errors**:
   - Run as administrator (Windows)
   - Check file permissions
   - Verify antivirus isn't blocking connections

#### Getting Help

- Check the [Troubleshooting Guide](troubleshooting.md)
- Submit an issue on GitHub
- Join our Discord community

## Next Steps

- Read the [User Guide](user-guide.md)
- Explore [Examples](examples/)
- Check out [API Reference](api-reference.md)
