import org.apache.iceberg.aws.s3.S3FileIO
import java.nio.charset.StandardCharsets
import scala.jdk.CollectionConverters._

val io = new S3FileIO()
io.initialize(Map(
  "s3.endpoint" -> "http://minio:9000",
  "s3.access-key-id" -> "admin",
  "s3.secret-access-key" -> "password",
  "s3.region" -> "us-east-1"
).asJava)

val out = io.newOutputFile("s3://warehouse/test_iceberg.txt").create()  // precisa criar com sucesso
out.write("Hello Iceberg + MinIO!".getBytes(StandardCharsets.UTF_8))
out.close()
