from mcp.server.fastmcp import FastMCP

mcp = FastMCP("helloworld")

@mcp.tool()
async def sum_two_numbers(a: int, b: int) -> int:
  return a + b

if __name__ == "__main__":
  mcp.run(transport='stdio')
