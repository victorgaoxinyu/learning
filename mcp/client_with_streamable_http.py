from typing import List, Any, Callable
from contextlib import AsyncExitStack

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client  # deprecated func...

class MCPClient:
    def __init__(self, name: str, server_url: str) -> None:
        self.name = name
        self.server_url = server_url
        self._session: ClientSession = None
        self._exit_stack = AsyncExitStack()
        self._connected: bool = False
        self._get_session_id: Callable[[], str] = None

    async def connect(self, headers: dict | None = None) -> None:
        if self._connected:
            raise RuntimeError("Client is already connected")
        
        # Connect to Streamable HTTP server
        streamable_connection = await self._exit_stack.enter_async_context(streamablehttp_client(url=self.server_url, headers=headers))
        self.read, self.write, self._get_session_id = streamable_connection

        # Start MCP client session
        self._session = await self._exit_stack.enter_async_context(ClientSession(read_stream=self.read, write_stream=self.write))
        
        # Init session
        await self._session.initialize()
        self._connected = True
    
    async def get_available_tools(self) -> List[Any]:
        pass

    async def use_tool(self, tool_name: str, tool_arg: List | None = None):
        pass

    async def disconnect(self) -> None:
        if self._exit_stack:
            await self._exit_stack.aclose()  # close all server connections in order
            self._connected = False
            self._session = None

