### Learning plan

- learn modern async web frameworks 
- create RESTful API with aiohttp
- ASGI, WSGI, Starlette
- create a simple REST API that support WebSocket
- stress test
- 

#### Use aiohttp create REST API

REST, representational state transfer

Connect to DB

- aiohttp.on_startup, aiohttp.on_cleanup

### ASGI

Asynchronous Server Gateway Interface

### WebSocket and Starlette

- get how many online user without keep refreshing
- using `persistent socket` instead of request/response cycle like HTTP
- bidirectional

coroutines we need to implement:

- on_connect
- on_receive
- on_disconnect

