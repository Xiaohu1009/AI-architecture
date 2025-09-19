# Cursor集成指南

## 概述

本指南将帮助您在Cursor IDE中配置和使用AI MCP Server，实现Rhino和Grasshopper的AI辅助设计功能。

## 前置要求

- Cursor IDE (最新版本)
- Python 3.10+
- Rhino 7+ (Windows/Mac)
- Grasshopper (随Rhino安装)

## 安装步骤

### 1. 安装MCP Server依赖

```bash
cd AI_mcp_server
pip install -e .
```

### 2. 配置Cursor MCP

#### 方法一：使用配置文件（推荐）

1. 复制 `cursor_mcp_config.json` 到Cursor的MCP配置目录
2. 根据您的实际安装路径修改 `cwd` 和 `PYTHONPATH` 路径

#### 方法二：手动配置

在Cursor的设置中添加MCP服务器配置：

```json
{
  "mcpServers": {
    "ai-mcp-server": {
      "command": "python",
      "args": ["run_server.py"],
      "cwd": "您的安装路径\\AI_mcp_server",
      "env": {
        "PYTHONPATH": "您的安装路径\\AI_mcp_server\\src"
      }
    }
  }
}
```

### 3. 启动MCP Server

在Cursor中，MCP服务器会自动启动。您可以在Cursor的MCP面板中看到服务器状态。

## 使用方法

### 在Cursor中使用AI工具

一旦配置完成，您就可以在Cursor中使用以下AI工具：

#### Rhino 3D建模工具
- `create_rhino_object` - 创建3D对象
- `modify_rhino_object` - 修改对象
- `get_rhino_document_info` - 获取文档信息
- `execute_rhino_script` - 执行RhinoScript

#### Grasshopper参数化设计工具
- `add_grasshopper_component` - 添加组件
- `connect_grasshopper_components` - 连接组件
- `create_grasshopper_pattern` - 创建参数化模式
- `get_grasshopper_document_info` - 获取文档信息

#### 统一工具
- `create_geometry` - 智能几何体创建
- `get_document_info` - 统一文档信息获取
- `sync_platforms` - 平台数据同步

### 示例用法

#### 创建3D几何体
```
请使用create_rhino_object工具创建一个10x10x5的盒子
```

#### 参数化设计
```
请使用create_grasshopper_pattern工具创建一个带有滑块的3D盒子参数化模型
```

#### 获取文档信息
```
请使用get_document_info工具获取当前Rhino文档的所有对象信息
```

## 故障排除

### 常见问题

1. **MCP服务器无法启动**
   - 检查Python路径是否正确
   - 确认所有依赖已安装
   - 查看Cursor的MCP日志

2. **Rhino/Grasshopper连接失败**
   - 确认Rhino正在运行
   - 检查端口1999和8080是否可用
   - 确认相应的插件已安装

3. **工具调用失败**
   - 检查Cursor的MCP面板中的错误信息
   - 确认服务器状态为"已连接"

### 调试模式

启用调试模式以获取详细日志：

```bash
# 设置环境变量
set AI_MCP_DEBUG=true
set AI_MCP_LOG_LEVEL=DEBUG

# 启动服务器
python run_server.py
```

## 高级配置

### 自定义端口

如果默认端口被占用，可以修改配置：

```json
{
  "mcpServers": {
    "ai-mcp-server": {
      "command": "python",
      "args": ["run_server.py"],
      "cwd": "您的安装路径\\AI_mcp_server",
      "env": {
        "PYTHONPATH": "您的安装路径\\AI_mcp_server\\src",
        "RHINO_PORT": "2999",
        "GRASSHOPPER_PORT": "9080"
      }
    }
  }
}
```

### 性能优化

- 使用SSD存储项目文件
- 确保有足够的内存（建议8GB+）
- 关闭不必要的Rhino插件

## 支持

如遇到问题，请：

1. 查看Cursor的MCP面板日志
2. 检查服务器控制台输出
3. 提交Issue到项目仓库

## 更新日志

- v1.0.0: 初始版本，支持Cursor集成
