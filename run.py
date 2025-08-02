from mcp.server.fastmcp import FastMCP
from utils.property_info import PropertyInfoRetriever
import requests

mcp = FastMCP("LOA")

@mcp.prompt()
def loa(user_name: str, user_title: str, user_workplace: str) -> str:
    """Global instructions for JOSH"""
    return f"""# LOA

You are Loa (Loan Officer Agent), a virtual assistant to {user_name} ({user_title}) at {user_workplace}. You are designed to help streamline the process
of originating loans. You are not done being built yet, but here are the current specifications.

** Your Capabilities **
- get the list price of a house using the house address

** My Preferences **
- very concise repsonses
- friendly tone
"""

@mcp.tool()
def get_list_price(property_address):
    property_info_retriever = PropertyInfoRetriever(property_address)
    return property_info_retriever.get_list_price()
    
if __name__ == '__main__':
    mcp.run(transport='stdio')