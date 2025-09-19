# AI MCP Server 快速开始指南

## 概述

AI MCP Server 是一个统一的 Model Context Protocol (MCP) 服务器，集成了 Rhino 和 Grasshopper 的功能，为 AI 代理提供完整的 3D 建模和参数化设计能力。

## 系统要求

- Python 3.10+
- Rhino 7+ (Windows/Mac)
- Grasshopper (随 Rhino 安装)

## 安装步骤

### 1. 克隆项目
```bash
git clone <repository-url>
cd AI_mcp_server
```

### 2. 安装依赖
```bash
pip install -e .
```

### 3. 启动服务器
```bash
# Windows
start_server.bat

# Linux/Mac
chmod +x start_server.sh
./start_server.sh

# 或者直接使用 Python
python run_server.py
```

## 配置 Claude Desktop

### 1. 找到 Claude Desktop 配置目录

**Windows:**
```
%APPDATA%\Claude\claude_desktop_config.json
```

**Mac:**
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

### 2. 编辑配置文件

将以下内容添加到 `claude_desktop_config.json`：

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

**重要**: 请将 `cwd` 路径更新为您的实际安装目录。

### 3. 重启 Claude Desktop

配置完成后，重启 Claude Desktop 以加载新的 MCP 服务器。

## 验证安装

启动服务器后，您应该看到类似以下的输出：

```
2025-09-19 17:14:21,391 - AIServer - INFO - All MCP tools registered
2025-09-19 17:14:21,391 - AIServer - INFO - AI MCP Server initialized: AI MCP Server v1.0.0
2025-09-19 17:14:21,391 - AIServer - INFO - Starting MCP server...
2025-09-19 17:14:21,397 - AIServer - INFO - Starting AI MCP Server...
2025-09-19 17:14:21,398 - AIServer - INFO - Initializing RhinoBridge
2025-09-19 17:14:23,451 - AIServer - ERROR - Failed to connect to 127.0.0.1:1999: [WinError 10061] 由于目标计算机积极拒绝，无法连接。
2025-09-19 17:14:21,398 - AIServer - INFO - Initializing GrasshopperBridge
2025-09-19 17:14:25,493 - AIServer - ERROR - Failed to connect to 127.0.0.1:8080: [WinError 10061] 由于目标计算机积极拒绝，无法连接。
2025-09-19 17:14:25,493 - AIServer - INFO - Rhino connection: Disconnected
2025-09-19 17:14:25,493 - AIServer - INFO - Grasshopper connection: Disconnected
2025-09-19 17:14:25,493 - AIServer - WARNING - Neither Rhino nor Grasshopper is connected. Some tools may not work.
```

这是正常的！服务器可以独立运行，即使没有连接到 Rhino 或 Grasshopper。

## 故障排除

### 问题：服务器无法启动
**解决方案**: 确保已安装所有依赖：
```bash
pip install -e .
```

### 问题：Claude Desktop 无法连接到服务器
**解决方案**: 
1. 检查配置文件中的路径是否正确
2. 确保服务器正在运行
3. 重启 Claude Desktop

### 问题：Rhino/Grasshopper 连接失败
**解决方案**: 这是正常的，因为需要相应的插件运行。服务器设计为即使没有连接也能工作。

## 下一步

- 查看 [README.md](../README.md) 了解完整功能
- 查看 [examples/](../examples/) 目录中的示例
- 阅读 [user-guide.md](user-guide.md) 获取详细使用说明
