# Microservice

### Learning Goal

- backend-for-frontend
- implement api with aioheep and asyncpg



### Backend-for-frontend

```
mobile client -->|backend for frontend|  --> all kinds of services 
web clienb    -->| service            |
```

### Implement product list API

#### User favourite service

- shopping cart
  - user id <-> product id
- stock
  - Product id <-> available stock
- product
  - product id <-> product info

Use `wait_for` coroutine function to handle retry 

### Circuit breaker pattern

- 当制定数量的错误在一定时间内发生时，使用断路器模式来绕过缓慢的服务，直到问题被解决

States:

- open
- close
- Half-open
  - when we are in open state after a certain time interval, we issue a single request to check if the issue with the service is fixed. If it is, we close the circuit breaker, if not, keep open.



