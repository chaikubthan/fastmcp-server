from fastmcp import FastMCP

app = FastMCP()

@app.tool()
def hello(name: str) -> str:
    return f"Hello, {name}! This is a FastMCP server from AWS via CI/CD"
