from fastmcp import FastMCP

mcp = FastMCP()

app = mcp.app()   # <<< จุดนี้คือ fix

@mcp.tool()
def hello(name: str) -> str:
    return f"Hello, {name}! This is a FastMCP server from AWS via CI/CD"
