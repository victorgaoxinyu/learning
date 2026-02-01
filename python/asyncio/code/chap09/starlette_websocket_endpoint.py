import asyncio
from starlette.applications import Starlette
from starlette.endpoints import WebSocketEndpoint
from starlette.routing import WebSocketRoute

class UserCounter(WebSocketEndpoint):
    encoding = 'text'
    sockets = []

    async def on_connect(self, websocket):
        await websocket.accept()
        print(websocket)
        UserCounter.sockets.append(websocket)
        print(len(UserCounter.sockets), UserCounter.sockets)
        await self._send_count()

    async def on_disconnect(self, websocket, close_code):
        UserCounter.sockets.remove(websocket)
        print(len(UserCounter.sockets))
        await self._send_count()
    
    async def on_receive(self, websocket, data):
        pass

    async def _send_count(self):
        if len(UserCounter.sockets) > 0:
            count_str = str(len(UserCounter.sockets))
            print("Count str: ", count_str, UserCounter.sockets)
            task_to_socekt = {
                asyncio.create_task(websocket.send_text(count_str)): websocket
                for websocket
                in UserCounter.sockets
            }

            done, pending = await asyncio.wait(task_to_socekt)

            for task in done:
                if task.exception is not None:
                    if task_to_socekt[task] in UserCounter.sockets:
                        print("Removing: ", task_to_socekt[task])
                        UserCounter.sockets.remove(task_to_socekt[task])

app = Starlette(routes=[WebSocketRoute('/counter', UserCounter)])