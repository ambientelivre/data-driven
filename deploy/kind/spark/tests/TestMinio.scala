

## foi copiada esta lib para o container spark
## rodar assim
## spark-shell --jars /opt/spark/jars/iceberg-rest-adapter.jar

## wget https://ambientelivre.com.br/treinamentos/iceberg-rest-adapter.jar


import org.apache.iceberg.Table
import org.apache.iceberg.Schema
import org.apache.iceberg.types.Types
import org.apache.iceberg.aws.s3.S3FileIO
import org.apache.iceberg.hadoop.HadoopTables // só se fosse Hadoop
import org.apache.iceberg.data.{GenericRecord, Record}
import org.apache.iceberg.data.parquet.GenericParquetWriter
import org.apache.iceberg.io.{FileIO, OutputFileFactory, FileAppender}
import scala.jdk.CollectionConverters._


val io = new S3FileIO()
io.initialize(Map(
  "s3.endpoint" -> "http://minio:9000",
  "s3.access-key-id" -> "admnin",
  "s3.secret-access-key" -> "password"
).asJava)

// Define o path da tabela
val tablePath = "s3://warehouse/test_minio_table/"

// Cria o esquema
val schema = new Schema(
  Types.NestedField.required(1, "id", Types.LongType.get()),
  Types.NestedField.required(2, "value", Types.StringType.get())
)

// Aqui você teria que criar a tabela via Iceberg API
import org.apache.iceberg.catalog.Namespace
import org.apache.iceberg.catalog.TableIdentifier
import org.apache.iceberg.catalog.Catalog
import org.apache.iceberg.rest.RESTCatalog

val catalogProps = Map(
  "uri" -> "http://rest:8181",
  "io-impl" -> "org.apache.iceberg.aws.s3.S3FileIO",
  "warehouse" -> "s3://warehouse/"
).asJava

val catalog = new RESTCatalog()
catalog.initialize("demo", catalogProps)
val ns = Namespace.of("cwb")

// Cria namespace se não existir
if (!catalog.namespaceExists(ns)) catalog.createNamespace(ns)

val tableId = TableIdentifier.of(ns, "taxis_test")
if (!catalog.tableExists(tableId)) {
  val table = catalog.createTable(tableId, schema)
}
