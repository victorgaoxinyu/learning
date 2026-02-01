from typing import List, Any


class MCPClient:
    # This could also be MCPServer, since from the perspective of the host
    # application, this object would represent an MCP Server
    def __init__(self):
        pass
        
    async def connect(self) -> None:
        pass
    
    async def get_available_tools(self) -> List[Any]:
        pass

    async def use_tool(self, tool_name: str, tool_arg: List | None = None):
        pass

    async def disconnect(self) -> None:
        pass


