"""Offline smoke test for the SDK dependency and all tool registrations."""

import asyncio


def test_server_registers_tools():
    from kanboard_mcp.config import Config, KanboardConfig
    from kanboard_mcp.server import create_server

    server = create_server(Config(kanboard=KanboardConfig(
        url="https://kanboard.example/jsonrpc.php", password="test-token"
    )))
    tools = asyncio.run(server.mcp.list_tools())
    names = {tool.name for tool in tools}
    assert "get_server_info" in names
    assert "test_connection" in names
    assert "getAllProjects" in names
