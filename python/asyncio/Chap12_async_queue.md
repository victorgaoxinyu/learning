### Learning Goal

- use aysncio queue to handle producer-consumer work flow
- 在后台工作的同时快速响应用户的请求
- 按优先级处理任务
- LIFO



### 处理队列的上下限

- 上限：队列有太多项目
  - OOM
  - use put coroutine method to put item into queue ONLY if we have enough space in the queue
- 下限：队列没有项目
  - 队列没有项目，会密集的轮训检查是否有项目，CPU密集
  - 使用get coroutine method to block the thread until a item in queue



### Queue in Web app

- create simple web app with aiohttp
  - use queue as backend
  - use sleep to simulate i/o with DB
  - API: create order
  - safe close up logic
  - 