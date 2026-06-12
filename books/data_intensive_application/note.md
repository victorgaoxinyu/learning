### Trade-Offs in Data System Architecture
Apps need:
- database
- caches
- search indexes
- stream processing
- batch processing
    - periodically, large amount, accmulated data


Operational V.S Analytical Systems

Operational:
- point query
- end user, create, update delete
- pre-defined queries
- OLTP: Online transaction processing

Analytical:
- aggregated
- bulk process or streaming
- unqiue, adhoc
- OLAP: Online analytical processing

HTAP: Hybrid transactional/analytical processing

#### Data warehouse -> Data Lake
The difference from a data warehouse is that a data lake simply contains files, without imposing any particular file format, data model, or schema


#### System of record and derived data
