### System scaling

#### Initial deployment
- Browser app: ReactJS browser app
- IOS app
- Android app
- stateless backend service
- SQL DB

GeoDNS
- **A Record**: DNS configuration that maps a domain to IP address
- find the best DC for different user IP, cached at various levels.

Caching Service
- Redis: certain backend endpoints with heavy traffice can be cached. 
- only request to DB if cache miss

Concent Distribution Network
- host static content/files out side of codebase
- fetch files from CDN
- various DC around world
- CloudFlare, Rackspace, AWS CloudFront

CI/CD and Infra-as-code
- Kubernetes
- Terraform, less vendor lockin

Gradually rollout and rollback

Experimentation
- A/B testing

Shared services
- logging: ElasticStack (ElasticSearch, Logstash, Kibana, Beats)
- distributed tracing system: trace request as it traverses through
- monitoring and alerting

API Gateway
- drawback: add latency, complex routing

Service Mesh
- sidecar
- sidecar-less

Command Query Reponsibility Segregation CQRS
- seperate Read and Write

#### Scaling DB
ACID
- Atomicity: all or nothing
- Consistency: must follow rules and constraints
- Isolation: operations are isolated, in seq env
- Durability: changes are permanent, even system crashed.

 “Objects smaller than 256K are best stored in a database while objects larger than 1M are best stored in the filesystem. Between 256K and 1M, the read:write ratio and rate of object overwrite or replacement are important factors.” 


Replications
- scale reads - increase the number of replicas
- single leader replication
    - write occur on single leader node
    - all about scaling read
- multi leader replication
    - handle race condition
    - single-writer ownership
    - version control
    - rules, (prefer xxx)
    - correctness is more important than write availability

Read Strategies
- Cache-Aside (Lazy Loading)
    - cache miss, write data to cache, slower than direct request
    - stale data, use TTL, or write-through (update the cache when write)

Write Strategies
- Write-through
    - write -> cache -> DB
    - slower, waste of cache, use TTL to reduce waste
- Write-Back/Behind
    - write -> cache -> batch up -> DB
    - complex, need high availability cache

Cache warming

#### Distributed transactions
TBC