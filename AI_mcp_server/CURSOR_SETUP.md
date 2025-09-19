# Cursor IDE 快速设置指南

## 为什么选择Cursor？

由于Claude在大陆地区无法使用，Cursor IDE是一个优秀的替代方案，它支持MCP协议，可以完美运行本AI MCP Server。

## 快速设置

### 1. 安装依赖
```bash
cd AI_mcp_server
pip install -e .
```

### 2. 配置Cursor

将以下配置添加到Cursor的MCP设置中：

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

**重要**：请将 `cwd` 路径修改为您的实际安装路径。

### 3. 验证设置

1. 重启Cursor IDE
2. 打开MCP面板，确认服务器状态为"已连接"
3. 尝试使用AI工具，例如：
   - "请创建一个10x10x5的盒子"
   - "获取当前Rhino文档信息"

## 可用的AI工具

### Rhino 3D建模
- 创建3D对象（点、线、圆、盒子、球体等）
- 修改和删除对象
- 执行RhinoScript
- 获取文档信息

### Grasshopper参数化设计
- 添加和连接组件
- 创建参数化模式
- 智能组件连接
- 数据流管理

### 统一工具
- 智能几何体创建
- 平台数据同步
- 批量操作支持

## 故障排除

### 服务器无法启动
- 检查Python路径
- 确认依赖已安装
- 查看Cursor MCP日志

### 连接失败
- 确认Rhino正在运行
- 检查端口1999和8080
- 确认插件已安装

## 更多信息

- 详细指南：[docs/cursor-integration-guide.md](docs/cursor-integration-guide.md)
- 项目文档：[README.md](README.md)
- 快速开始：[docs/quick-start-guide.md](docs/quick-start-guide.md)

## 支持

如遇问题，请查看Cursor的MCP面板日志或提交Issue。
