from mcp.server.fastmcp import FastMCP
import sqlite3
from random import choice

mcp = FastMCP("Get Travel Tips")

DB_PATH = "travel.db"

@mcp.tool()
def get_travel_tip() -> str:
    """
    Returns a random travel tip from the SQLite database
    when the user asks about travelling.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT tip FROM travel_tips")
    tips = [row[0] for row in cursor.fetchall()]

    conn.close()

    if not tips:
        return "No travel tips available."

    return choice(tips)

"""
@mcp.tool()
def get_travel_tip() -> str:
    travel_tips = [
        "Keep digital copies of important documents.",
        "Pack light and leave space for souvenirs.",
        "Always carry a reusable water bottle.",
        "Check local customs before you travel.",
        "Keep emergency contacts saved offline.",
        "Arrive at the airport early for international flights."
    ]

    return choice(travel_tips)

if __name__ == "__main__":
    mcp.run()
"""