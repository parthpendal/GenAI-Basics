from mcp.server.fastmcp import FastMCP

mcp=FastMCP(name="math")

@mcp.tool()
def add(a:int,b:int)->int:
    """Add two numbers together"""
    return a+b

@mcp.tool()
def subtract(a:int,b:int)->int:
    """Subtract second numbers from first"""
    return a-b

@mcp.tool()
def multiply(a:int,b:int)->int:
    """Multiply two numbers together"""
    return a*b

@mcp.tool()
def divide(a:int,b:int)->float:
    """Divide first number by second"""
    return a/b

if __name__ == "__main__":
    mcp.run(transport="stdio")
#Transport is the way the MCP server communicates with the client.
#stdio is the standard input and output of the command line.
#We can also use other transports like websockets, http, etc.
#websockets is used in the browser.
