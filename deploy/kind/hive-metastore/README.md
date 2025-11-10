
helm repo add trino https://trinodb.github.io/charts

helm upgrade --install trino-cluster trino/trino \
  -f values.yaml \
  --namespace trino \
  --post-renderer ./remove-keystore.sh



## Build Hive Image

cd /opt/trino/kind/metastore

docker build -t kind-registry:5000/hive_metastore_postgres:1.0.0 .
docker tag kind-registry:5000/hive_metastore_postgres:1.0.0 localhost:5000/hive_metastore_postgres:1.0.0

docker push localhost:5000/hive_metastore_postgres:1.0.0

https://medium.com/@stefentaime_10958/my-adventure-with-apache-iceberg-migrating-a-local-hive-data-warehouse-poc-b494a50a04b5
