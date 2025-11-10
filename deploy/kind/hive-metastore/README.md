
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


## COmandos para Debug
### Criando o Schema direto pelo Hive.

hive --service metatool
ou
hive --service cli -e "CREATE DATABASE teste LOCATION 's3a://warehouse/teste';"

hadoop fs -ls s3a://warehouse/








## Build Hive Image

cd /opt/trino/kind/metastore

docker build -t kind-registry:5000/hive_metastore_postgres:1.0.0 .
docker tag kind-registry:5000/hive_metastore_postgres:1.0.0 localhost:5000/hive_metastore_postgres:1.0.0

docker push localhost:5000/hive_metastore_postgres:1.0.0

https://medium.com/@stefentaime_10958/my-adventure-with-apache-iceberg-migrating-a-local-hive-data-warehouse-poc-b494a50a04b5
