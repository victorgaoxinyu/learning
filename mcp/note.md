### Basic Client Design

At least implement:
- Connect to a server
- Discover the server's resources
- Make resources available to LLM

Also important
- Authentication
- Resource filtering
- Model agnosticism

Transport layer
- stdio
  - server run alongside host app
- streamable http
  - more versatile

`AsyncExitStack` allows manually nest async context manager without using `async with`.
Can dynamically add more async context manager and safely release all resources on the stack in order with just one call.
`enter_async_context()`

Connection Code:
1. create instance of `StdioServerParams`
2. start stdio server subprocess in async
3. start mcp client in async
4. init session