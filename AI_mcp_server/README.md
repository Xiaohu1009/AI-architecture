# AI MCP Server - Unified Rhino & Grasshopper Integration

[English](#english) | [中文](#中文)

## English

AI MCP Server is a unified Model Context Protocol (MCP) server that integrates both Rhino and Grasshopper functionality, providing AI agents with comprehensive 3D modeling and parametric design capabilities.

### Key Features

#### 🎯 Unified Interface
- Single MCP server supporting both Rhino and Grasshopper
- Smart routing: automatically selects target platform based on operation type
- Unified error handling and logging

#### 🏗️ Rhino 3D Modeling
- **Object Creation**: Points, lines, circles, arcs, ellipses, curves, boxes, spheres, cones, cylinders, surfaces
- **Object Operations**: Modify, delete, select objects
- **Document Management**: Get document info, layer management
- **Script Execution**: Execute RhinoScript Python code
- **Object Queries**: Get object info, selected objects info

#### 🔧 Grasshopper Parametric Design
- **Component Management**: Add, connect, query components
- **Parametric Modeling**: Create complex parametric geometries
- **Pattern Recognition**: Create component patterns based on high-level descriptions
- **Smart Connections**: Automatically handle data flow connections between components

#### 🚀 Advanced Features
- **Smart Routing**: Automatically select Rhino or Grasshopper based on operation type
- **Data Conversion**: Convert geometric data between Rhino and Grasshopper
- **Batch Operations**: Support batch creation and modification of objects
- **Real-time Sync**: Keep data synchronized between both platforms

### System Architecture

```
AI MCP Server
├── Core Server (Python FastMCP)
├── Rhino Bridge (TCP: 1999)
├── Grasshopper Bridge (TCP: 8080)
└── Unified API Layer
```

### Requirements

- Python 3.10+
- Rhino 7+ (Windows/Mac)
- Grasshopper (installed with Rhino)
- uv package manager

### Quick Start

1. **Install Dependencies**
   ```bash
   pip install -e .
   ```

2. **Start Server**
   ```bash
   # Option 1: Direct Python
   python run_server.py
   
   # Option 2: Use startup script (Windows)
   start_server.bat
   
   # Option 3: Use startup script (Linux/Mac)
   chmod +x start_server.sh
   ./start_server.sh
   ```

3. **Configure AI Client**
   
   #### For Cursor IDE (Recommended for Chinese users)
   ```json
   {
     "mcpServers": {
       "ai-mcp-server": {
         "command": "python",
         "args": ["run_server.py"],
         "cwd": "D:\\mcp_sever\\AI_mcp_server",
         "env": {
           "PYTHONPATH": "D:\\mcp_sever\\AI_mcp_server\\src"
         }
       }
     }
   }
   ```
   
   #### For Claude Desktop
   ```json
   {
     "mcpServers": {
       "ai-mcp-server": {
         "command": "python",
         "args": ["run_server.py"],
         "cwd": "D:\\mcp_sever\\AI_mcp_server"
       }
     }
   }
   ```
   
   **Note**: Update the `cwd` path to match your actual installation directory.
   
   Configuration files are provided:
   - `cursor_mcp_config.json` - For Cursor IDE
   - `claude_desktop_config.json` - For Claude Desktop

📖 **Quick Start Guide**: See [docs/quick-start-guide.md](docs/quick-start-guide.md) for detailed setup instructions.  
📖 **Cursor Integration Guide**: See [docs/cursor-integration-guide.md](docs/cursor-integration-guide.md) for Cursor-specific setup.

### Usage Examples

#### Create 3D Geometry
```python
# Create box in Rhino
create_rhino_object(type="BOX", params={"width": 10, "length": 10, "height": 5})

# Create parametric box in Grasshopper
create_grasshopper_pattern("3D box with sliders")
```

#### Data Conversion
```python
# Get geometry from Rhino and use in Grasshopper
rhino_objects = get_rhino_document_info()
convert_to_grasshopper_components(rhino_objects)
```

### Tool Categories

#### Rhino Tools
- `create_rhino_object` - Create 3D objects
- `modify_rhino_object` - Modify objects
- `get_rhino_document_info` - Get document info
- `execute_rhino_script` - Execute scripts

#### Grasshopper Tools
- `add_grasshopper_component` - Add components
- `connect_grasshopper_components` - Connect components
- `create_grasshopper_pattern` - Create patterns
- `get_grasshopper_document_info` - Get document info

#### Unified Tools
- `create_geometry` - Smart geometry creation
- `get_document_info` - Unified document info
- `sync_platforms` - Sync platform data

### Development

#### Project Structure
```
AI_mcp_server/
├── src/
│   ├── ai_mcp_server/
│   │   ├── core/           # Core server
│   │   ├── bridges/        # Platform bridges
│   │   ├── tools/          # MCP tools
│   │   └── utils/          # Utility functions
│   └── tests/              # Tests
├── docs/                   # Documentation
└── examples/              # Examples
```

#### Contributing
1. Fork the project
2. Create a feature branch
3. Commit your changes
4. Create a Pull Request

### License

MIT License - see LICENSE file for details

### Support

For issues or suggestions, please submit an Issue or contact the development team.

### Current Status

✅ **Server Successfully Running**: The AI MCP server can now start properly  
✅ **Tools Registered**: All MCP tools are correctly registered  
✅ **Connection Detection**: Server can detect Rhino and Grasshopper connection status  
✅ **Graceful Shutdown**: Supports Ctrl+C graceful shutdown  

**Note**: The server shows that Rhino (port 1999) and Grasshopper (port 8080) are not connected, which is normal since:
- These ports require corresponding Rhino and Grasshopper plugins to be running
- The server is designed to run even without connections, with tools showing connection errors when platforms are unavailable

## 中文

AI MCP Server是一个统一的Model Context Protocol (MCP)服务器，集成了Rhino和Grasshopper的功能，为AI代理提供完整的3D建模和参数化设计能力。

## 功能特性

### 🎯 统一接口
- 单一MCP服务器同时支持Rhino和Grasshopper
- 智能路由：根据操作类型自动选择目标平台
- 统一的错误处理和日志记录

### 🏗️ Rhino 3D建模
- **对象创建**：点、线、圆、弧、椭圆、曲线、盒子、球体、圆锥、圆柱、表面等
- **对象操作**：修改、删除、选择对象
- **文档管理**：获取文档信息、图层管理
- **脚本执行**：执行RhinoScript Python代码
- **对象查询**：获取对象信息、选择对象信息

### 🔧 Grasshopper参数化设计
- **组件管理**：添加、连接、查询组件
- **参数化建模**：创建复杂的参数化几何体
- **模式识别**：基于高级描述创建组件模式
- **智能连接**：自动处理组件间的数据流连接

### 🚀 高级功能
- **智能路由**：根据操作类型自动选择Rhino或Grasshopper
- **数据转换**：在Rhino和Grasshopper之间转换几何数据
- **批量操作**：支持批量创建和修改对象
- **实时同步**：保持两个平台之间的数据同步

## 系统架构

```
AI MCP Server
├── Core Server (Python FastMCP)
├── Rhino Bridge (TCP: 1999)
├── Grasshopper Bridge (TCP: 8080)
└── Unified API Layer
```

## 安装要求

- Python 3.10+
- Rhino 7+ (Windows/Mac)
- Grasshopper (随Rhino安装)
- uv包管理器

## 快速开始

1. **安装依赖**
   ```bash
   pip install -e .
   ```

2. **启动服务器**
   ```bash
   # 方式1：直接使用Python
   python run_server.py
   
   # 方式2：使用启动脚本 (Windows)
   start_server.bat
   
   # 方式3：使用启动脚本 (Linux/Mac)
   chmod +x start_server.sh
   ./start_server.sh
   ```

3. **配置AI客户端**
   
   #### 对于Cursor IDE（推荐中国用户使用）
   ```json
   {
     "mcpServers": {
       "ai-mcp-server": {
         "command": "python",
         "args": ["run_server.py"],
         "cwd": "D:\\mcp_sever\\AI_mcp_server",
         "env": {
           "PYTHONPATH": "D:\\mcp_sever\\AI_mcp_server\\src"
         }
       }
     }
   }
   ```
   
   #### 对于Claude Desktop
   ```json
   {
     "mcpServers": {
       "ai-mcp-server": {
         "command": "python",
         "args": ["run_server.py"],
         "cwd": "D:\\mcp_sever\\AI_mcp_server"
       }
     }
   }
   ```
   
   **注意**：请更新`cwd`路径以匹配您的实际安装目录。
   
   提供的配置文件：
   - `cursor_mcp_config.json` - 用于Cursor IDE
   - `claude_desktop_config.json` - 用于Claude Desktop

📖 **快速开始指南**: 查看 [docs/quick-start-guide.md](docs/quick-start-guide.md) 获取详细的设置说明。  
📖 **Cursor集成指南**: 查看 [docs/cursor-integration-guide.md](docs/cursor-integration-guide.md) 获取Cursor专用设置说明。

## 使用示例

### 创建3D几何体
```python
# 在Rhino中创建盒子
create_rhino_object(type="BOX", params={"width": 10, "length": 10, "height": 5})

# 在Grasshopper中创建参数化盒子
create_grasshopper_pattern("3D box with sliders")
```

### 数据转换
```python
# 从Rhino获取几何体并在Grasshopper中使用
rhino_objects = get_rhino_document_info()
convert_to_grasshopper_components(rhino_objects)
```

## 工具分类

### Rhino工具
- `create_rhino_object` - 创建3D对象
- `modify_rhino_object` - 修改对象
- `get_rhino_document_info` - 获取文档信息
- `execute_rhino_script` - 执行脚本

### Grasshopper工具
- `add_grasshopper_component` - 添加组件
- `connect_grasshopper_components` - 连接组件
- `create_grasshopper_pattern` - 创建模式
- `get_grasshopper_document_info` - 获取文档信息

### 统一工具
- `create_geometry` - 智能创建几何体
- `get_document_info` - 获取统一文档信息
- `sync_platforms` - 同步平台数据

## 开发

### 项目结构
```
AI_mcp_server/
├── src/
│   ├── ai_mcp_server/
│   │   ├── core/           # 核心服务器
│   │   ├── bridges/        # 平台桥接
│   │   ├── tools/          # MCP工具
│   │   └── utils/          # 工具函数
│   └── tests/              # 测试
├── docs/                   # 文档
└── examples/              # 示例
```

### 贡献指南
1. Fork项目
2. 创建功能分支
3. 提交更改
4. 创建Pull Request

## 许可证

MIT License - 详见LICENSE文件

## 支持

如有问题或建议，请提交Issue或联系开发团队。

## 当前状态

✅ **服务器成功运行**：AI MCP服务器现在可以正常启动  
✅ **工具注册完成**：所有MCP工具都已正确注册  
✅ **连接检测**：服务器能够检测Rhino和Grasshopper的连接状态  
✅ **优雅关闭**：支持Ctrl+C优雅关闭  

**说明**：服务器显示Rhino (端口1999) 和 Grasshopper (端口8080) 都未连接，这是正常的，因为：
- 这些端口需要相应的Rhino和Grasshopper插件运行
- 服务器设计为即使没有连接也能运行，只是相关工具会显示连接错误

## 使用方法

现在您可以通过以下方式启动服务器：
```bash
cd AI_mcp_server
python run_server.py
```

服务器将使用stdio传输协议运行，可以与MCP客户端（如Claude Desktop）集成。
