
## Helm Trino
helm repo add trino https://trinodb.github.io/charts

```sh
helm upgrade --install trino-cluster trino/trino \
  -f values.yaml \
  --namespace trino \
  --post-renderer ./remove-keystore.sh
```

trino --server https://localhost:8443 --user admin --password --insecure

CREATE SCHEMA iceberg.nataltrino
WITH (location = 's3a://warehouse/nataltrino/');

CREATE TABLE iceberg.nataltrino.taxis (
  vendor_id BIGINT,
  trip_id BIGINT,
  trip_distance DOUBLE,
  fare_amount DOUBLE,
  store_and_fwd_flag VARCHAR
);


## Comandos para Debug
### Criando o Schema direto pelo Hive.

hive --service metatool
ou
hive --service cli -e "CREATE DATABASE teste LOCATION 's3a://warehouse/teste';"

hadoop fs -ls s3a://warehouse/

----------------dentro do container do Hive------

export AWS_ACCESS_KEY=minio
export AWS_SECRET_ACCESS_KEY=sejalivre
hadoop fs -ls s3a://warehouse/



Erros possiveis:

2025-11-10 18:17:54,536 INFO impl.MetricsConfig: Loaded properties from hadoop-metrics2.properties
2025-11-10 18:17:54,693 INFO impl.MetricsSystemImpl: Scheduled Metric snapshot period at 10 second(s).
2025-11-10 18:17:54,693 INFO impl.MetricsSystemImpl: s3a-file-system metrics system started
ls: s3a://warehouse/: listStatus on s3a://warehouse/: com.amazonaws.services.s3.model.AmazonS3Exception: The AWS Access Key Id you provided does not exist in our records. (Service: Amazon S3; Status Code: 403; Error Code: InvalidAccessKeyId; Request ID: QMAPSSZ304PRGT7W; S3 Extended Request ID: 8KqIzyytD3VtSB4rkozXCPN+f8K5mAWCudSk+jV5wXtOpimmBRiW/j38teUMKbEuKJrfjxstJWI=; Proxy: null), S3 Extended Request ID: 8KqIzyytD3VtSB4rkozXCPN+f8K5mAWCudSk+jV5wXtOpimmBRiW/j38teUMKbEuKJrfjxstJWI=:InvalidAccessKeyId
2025-11-10 18:18:00,097 INFO impl.MetricsSystemImpl: Stopping s3a-file-system metrics system...
2025-11-10 18:18:00,099 INFO impl.MetricsSystemImpl: s3a-file-system metrics system stopped.
2025-11-10 18:18:00,100 INFO impl.MetricsSystemImpl: s3a-file-system metrics system shutdown complete.








## Build Hive Image

cd /opt/trino/kind/metastore

docker build -t kind-registry:5000/hive_metastore_postgres:1.0.0 .
docker tag kind-registry:5000/hive_metastore_postgres:1.0.0 localhost:5000/hive_metastore_postgres:1.0.0

docker push localhost:5000/hive_metastore_postgres:1.0.0

https://medium.com/@stefentaime_10958/my-adventure-with-apache-iceberg-migrating-a-local-hive-data-warehouse-poc-b494a50a04b5
