# mcp/client.py

from mcp.server import execute


def call_tool(tool_name, query):

    return execute(tool_name, query)