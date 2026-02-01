from typing import List, Any
from contextlib import AsyncExitStack

from mcp import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client


class MCPClient:
    # This could also be MCPServer, since from the perspective of the host
    # application, this object would represent an MCP Server
    def __init__(self, name: str, command: str, server_args: List[str], env_vars: dict[str, str]=None) -> None:
        self.name = name
        self.command = command  # python/node/npx...
        self.server_args = server_args  # --port, --verbose...
        self.env_vars = env_vars  # {**os.env}
        self._session: ClientSession = None
        self._exit_stack: AsyncExitStack = AsyncExitStack()
        self._connected: bool = False
        
    async def connect(self) -> None:
        if self._connected:
            raise RuntimeError("Client is already connected")
        
        server_paramters = StdioServerParameters(
            command=self.command,
            args=self.server_args,
            env=self.env_vars or None
        )

        # Connect to stdio server, starting subprocess
        stdio_connection = await self._exit_stack.enter_async_context(stdio_client(server_paramters))
        self.read, self.write = stdio_connection

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

