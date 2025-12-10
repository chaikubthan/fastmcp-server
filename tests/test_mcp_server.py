import pytest
import os
from langchain_mcp_adapters.client import MultiServerMCPClient

# Read host + port/path from environment variables
EC2_HOST = os.environ.get("EC2_HOST")
MCP_PORT = os.environ.get("MCP_PORT")  # example: "3000/mcp"

# Build full URL: http://host:port/path
SERVER_URL = f"http://{EC2_HOST}:{MCP_PORT}" if EC2_HOST and MCP_PORT else None

@pytest.mark.asyncio
async def test_get_tools():
    assert SERVER_URL is not None, "Missing EC2_HOST or MCP_PORT environment variables!"

    client = MultiServerMCPClient(
        {
            "Multitool": {
                "url": SERVER_URL,
                "transport": "streamable_http",
            }
        }
    )

    tools = await client.get_tools()

    assert isinstance(tools, dict)
    assert len(tools["Multitool"]) > 0
