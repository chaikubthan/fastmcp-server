import os
import pytest
from langchain_mcp_adapters.client import MultiServerMCPClient
import time

@pytest.mark.asyncio
async def test_local_mcp_server():
    start = time.time()
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
    duration = round((time.time() - start) * 1000, 2)  # ms latency

    
    assert "health_check" in tool_names
    
    print("\n✅ test_get_tools PASSED — LOCAL MCP server is working correctly!\n")
    print(f"LATENCY_MS={duration}")
    print(f"TOOL_LIST={tool_names}")    
