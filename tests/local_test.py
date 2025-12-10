import os
import pytest
from langchain_mcp_adapters.client import MultiServerMCPClient

@pytest.mark.asyncio
async def test_local_mcp_server():
    client = MultiServerMCPClient(
        {
            "Multitool": {
                "url": os.environ["MCP_URL"],
                "transport": "streamable_http",
            }
        }
    )

    tools = await client.get_tools()
    tool_names = [t.name for t in tools]

    assert "health_check" in tool_names
