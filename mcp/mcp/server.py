# mcp/server.py

from mcp.registry import get_tool


def execute(tool_name, query):

    tool = get_tool(tool_name)

    if tool is None:
        return {
            "status": "error",
            "message": f"{tool_name} tool not found"
        }

    return tool(query)