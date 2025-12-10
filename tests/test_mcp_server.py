import pytest
import os
from langchain_mcp_adapters.client import MultiServerMCPClient
import time

EC2_HOST = os.environ.get("EC2_HOST")
MCP_PORT = os.environ.get("MCP_PORT")

SERVER_URL = f"http://{EC2_HOST}:{MCP_PORT}" if EC2_HOST and MCP_PORT else None

@pytest.mark.asyncio
async def test_get_tools():
    assert SERVER_URL is not None, "Missing EC2_HOST or MCP_PORT environment variables!"
    start = time.time()
    client = MultiServerMCPClient(
        {
            "Multitool": {
                "url": SERVER_URL,
                "transport": "streamable_http",
            }
        }
    )

    tools = await client.get_tools()
    duration = round((time.time() - start) * 1000, 2)  # ms latency
    
    # 1) get_tools() must return a list
    assert isinstance(tools, list), f"Expected list but got {type(tools)}"

    # 2) list must not be empty
    assert len(tools) > 0, "Tools list is empty!"

    # 3) validate each element is a StructuredTool
    for t in tools:
        assert hasattr(t, "name"), "Tool object has no name"
        assert hasattr(t, "description"), "Tool object has no description"

    # 4) ensure expected tools exist
    tool_names = [t.name for t in tools]
    expected_tools = ["health_check"]

    for et in expected_tools:
        assert et in tool_names, f"Missing tool: {et}"

    # Print to stdout so CI report can read it
    print("\n✅ test_get_tools PASSED — MCP server is working correctly!\n")
    print(f"LATENCY_MS={duration}")
    print(f"TOOL_LIST={tool_names}")    
