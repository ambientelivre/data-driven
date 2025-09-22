
## Instalar Parquet

wget https://repo1.maven.org/maven2/org/apache/nifi/nifi-parquet-nar/2.5.0/nifi-parquet-nar-2.5.0.nar

wget https://repo1.maven.org/maven2/org/apache/nifi/nifi-hadoop-libraries-nar/2.5.0/nifi-hadoop-libraries-nar-2.5.0.nar

## Fazer o build 

docker build -t localhost:5000/nifi:2.5.0-parquet .

docker tag localhost:5000/nifi:2.5.0-parquet localhost:5000/nifi:2.5.0-parquet

docker push localhost:5000/nifi:2.5.0-parquet


mudar no deploy do Nifi

  clusterImage: kind-registry:5000/nifi:2.5.0-parquet

