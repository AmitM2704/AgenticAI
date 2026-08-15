# mcp/registry.py

from mcp.tools.weather import run as weather_tool
from mcp.tools.calendar import run as calendar_tool
from mcp.tools.email import run as email_tool


TOOLS = {
    "weather": weather_tool,
    "calendar": calendar_tool,
    "email": email_tool
}


def get_tool(tool_name):
    return TOOLS.get(tool_name)


def list_tools():
    return list(TOOLS.keys())