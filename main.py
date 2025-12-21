from typing import List
from mcp.server.fastmcp import FastMCP
import os
from datetime import datetime

PORT = int(os.environ.get("PORT", 3000))

# Initialize FastMCP server
mcp = FastMCP("Multitool", host="0.0.0.0", port=PORT)

@mcp.tool()
async def health_check() -> str:
    """Check server health"""
    return "ok"

@mcp.tool()
async def get_weather(location: str) -> str:
    """Get weather for location."""
    return "It's always sunny in New York"

@mcp.tool()
async def get_city(location: str) -> str:
    """Get city name."""
    return "Newyork wtf"
    
@mcp.tool()
async def add(a: int, b: int) -> int:
    return a + b

@mcp.tool()
async def multiply(a: int, b: int) -> int:
    return a * b

@mcp.tool()
async def subtract(a: int, b: int) -> int:
    return a - b

@mcp.tool()
async def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

@mcp.tool()
async def today_date() -> str:
    today = datetime.today()
    return today.strftime("%Y-%m-%d")

if __name__ == "__main__":
    print(f"Starting MCP server on 0.0.0.0:{PORT}")
    mcp.run(transport="streamable-http")
