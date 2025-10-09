##

### Testing

´´´shell
$SPARK_HOME/bin/spark-sql \
  --master spark://cluster-with-hpa-template-master-0:7077 \
  --conf spark.sql.catalog.iceberg=org.apache.iceberg.spark.SparkCatalog \
  --conf spark.sql.catalog.iceberg.type=rest \
  --conf spark.sql.catalog.iceberg.uri=http://iceberg-rest-catalog.spark.svc.cluster.local:8181 \
  --conf spark.sql.catalog.iceberg.warehouse=s3a://warehouse/ \
  --conf spark.hadoop.fs.s3a.endpoint=http://minio-data-driven-hl.tenant-data-driven.svc.cluster.local:9000 \
  --conf spark.hadoop.fs.s3a.access.key=minio \
  --conf spark.hadoop.fs.s3a.secret.key=minio123 \
  --conf spark.hadoop.fs.s3a.path.style.access=true \
  --conf spark.hadoop.fs.s3a.impl=org.apache.hadoop.fs.s3a.S3AFileSystem \
  --conf spark.sql.defaultCatalog=iceberg
  ´´´
