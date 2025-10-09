## Deloy

### Testing
```shell
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
  ``

```shell
CREATE NAMESPACE IF NOT EXISTS nyc;


CREATE TABLE nyc.taxis (
  vendor_id BIGINT,
  trip_id BIGINT,
  trip_distance FLOAT,
  fare_amount DOUBLE,
  store_and_fwd_flag STRING
) ;


INSERT INTO iceberg.nyc2.taxis VALUES
  (1, 1001, 5.2, 15.5, 'N'),
  (2, 1002, 3.8, 10.0, 'Y'),
  (1, 1003, 12.0, 25.0, 'N');
```

