import org.apache.iceberg.aws.s3.S3FileIO
import java.nio.charset.StandardCharsets
import java.io.OutputStream

// Cria a instância do FileIO do Iceberg
val io = new S3FileIO()

// Inicializa com as credenciais do MinIO
import scala.jdk.CollectionConverters._
io.initialize(Map(
  "s3.endpoint" -> "http://minio:9000",
  "s3.access-key-id" -> "admin",
  "s3.secret-access-key" -> "password"
).asJava)

// Caminho do "arquivo teste" no bucket
val path = "s3://warehouse/test_iceberg.txt"

// Escreve algo simples no MinIO
val out: OutputStream = io.newOutputFile(path).create()
out.write("Hello Iceberg + MinIO!".getBytes(StandardCharsets.UTF_8))
out.close()

// Verifique no MinIO se o arquivo foi criado
println(s"Arquivo criado em: $path")
