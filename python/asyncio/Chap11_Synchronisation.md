- Synchronisation primitives 
  - 同步原语

### Learning Goal

- introduce race conditions and solve them using
  - lock
  - other sync preimitives
- Use semaphores to limit concurrency
  - ocntrol access to shared resources



### Single thread concurrent issue

- 以错误的顺序执行多个操作可能导致其他问题

模拟用户在发送消息的时候断开连接

单线程并发模型中常见：

- 在await达到挂起点，另一个协程运行并修改共享状态，第一个协程恢复时就会发生修改冲突



### Use asyncio lock

- awaitable
- 当一个协程在等待获得lock的时候，其他的代码可以运行
- async context manager



### Semaphore

- to avoid peak, use traffic-shaping
  - leaky bucket, token bucket
- use BoundedSemaphore to avoid release too many times
  - release too many time can accidentally add available number of sempahore.

### Example

- 构建一个API来接受客户端上传文件

### Conditions

- 继续或者只唤醒特定数量的任务（而不是所有任务）

