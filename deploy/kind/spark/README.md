## Deploy

### Testing
```shell
$SPARK_HOME/bin/spark-sql \
  --master spark://cluster-with-hpa-template-master-0:7077 \
  --conf spark.sql.catalog.iceberg=org.apache.iceberg.spark.SparkCatalog \
  --conf spark.sql.catalog.iceberg.type=rest \
  --conf spark.sql.catalog.iceberg.uri=http://iceberg-rest-catalog.spark.svc.cluster.local:8181 \
  --conf spark.sql.catalog.iceberg.warehouse=s3a://warehouse/ \
  --conf spark.sql.defaultCatalog=iceberg \
  --conf spark.sql.warehouse.dir=s3a://warehouse/ \
  --conf spark.sql.catalog.iceberg.io-impl=org.apache.iceberg.aws.s3.S3FileIO \
  --conf spark.sql.catalog.demo.s3.endpoint=http://minio:9000
  ```

```shell


paga S3a:
  --conf spark.hadoop.fs.s3a.endpoint=http://minio-data-driven-hl.tenant-data-driven.svc.cluster.local:9000 \
 --conf spark.hadoop.fs.s3a.access.key=minio \
  --conf spark.hadoop.fs.s3a.secret.key=minio123 \
  --conf spark.hadoop.fs.s3a.path.style.access=true \
  --conf spark.hadoop.fs.s3a.impl=org.apache.hadoop.fs.s3a.S3AFileSystem \

CREATE NAMESPACE IF NOT EXISTS nyc;


CREATE TABLE nyc.taxis (
  vendor_id BIGINT,
  trip_id BIGINT,
  trip_distance FLOAT,
  fare_amount DOUBLE,
  store_and_fwd_flag STRING
) ;


CREATE TABLE nyc.taxis (
  vendor_id BIGINT,
  trip_id BIGINT,
  trip_distance FLOAT,
  fare_amount DOUBLE,
  store_and_fwd_flag STRING
) USING iceberg
LOCATION 's3://warehouse/nyc/taxis/';


INSERT INTO iceberg.nyc.taxis VALUES
  (1, 1001, 5.2, 15.5, 'N'),
  (2, 1002, 3.8, 10.0, 'Y'),
  (1, 1003, 12.0, 25.0, 'N');
```

```java
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.types._

// Cria SparkSession
val spark = SparkSession.builder()
  .appName("SparkMinioTest")
  .master("local[*]")
  .getOrCreate()

// Configurações do MinIO (S3A)
spark.sparkContext.hadoopConfiguration.set("fs.s3a.endpoint", "http://localhost:9000")
spark.sparkContext.hadoopConfiguration.set("fs.s3a.access.key", "minio")
spark.sparkContext.hadoopConfiguration.set("fs.s3a.secret.key", "minio123")
spark.sparkContext.hadoopConfiguration.set("fs.s3a.path.style.access", "true")
spark.sparkContext.hadoopConfiguration.set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")

// Cria um DataFrame de exemplo
val schema = StructType(Array(
  StructField("id", IntegerType, true),
  StructField("name", StringType, true)
))

val data = Seq(
  (1, "Alice"),
  (2, "Bob"),
  (3, "Charlie")
)

val df = spark.createDataFrame(data).toDF("id", "name")

// Caminho no MinIO (pode ser s3a://bucket/pasta/)
val minioPath = "s3a://warehouse/test-data/"

// Escreve no MinIO
df.write.mode("overwrite").parquet(minioPath)

// Lê do MinIO
val readDf = spark.read.parquet(minioPath)
readDf.show()
```
