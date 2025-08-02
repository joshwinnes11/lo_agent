from mcp.server.fastmcp import FastMCP
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
- three different quote options:
    - conservative
    - standard
    - aggressive
"""

@mcp.tool()
def get_property_price(property_address):
    url = "https://zillow-com1.p.rapidapi.com/zestimate"
    payload = {"address": property_address}
    headers = {
        "x-rapidapi-key": "268487c947mshee2b17b8a5f2e29p1b21ddjsnc38181cb880b",
        "x-rapidapi-host": "zillow-com1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=payload).json()
    return response
    
if __name__ == '__main__':
    mcp.run(transport='stdio')