FROM quay.io/strimzi/kafka:0.47.0-kafka-4.0.0

# Define diretório dos plugins
ENV KAFKA_CONNECT_PLUGINS_DIR=/opt/kafka/plugins
RUN mkdir -p $KAFKA_CONNECT_PLUGINS_DIR

USER root

# Plugin connect-file
RUN mkdir -p $KAFKA_CONNECT_PLUGINS_DIR/connect-file
COPY libs/connect-file-4.0.0.jar $KAFKA_CONNECT_PLUGINS_DIR/connect-file/connect-file-4.0.0.jar

# Plugin postgres 3.2.2 
RUN mkdir -p $KAFKA_CONNECT_PLUGINS_DIR/postgres
COPY libs/debezium-connector-postgres-3.2.2.Final.jar $KAFKA_CONNECT_PLUGINS_DIR/postgres/debezium-connector-postgres-3.2.2.Final.jar
COPY libs/protobuf-java-3.25.5.jar $KAFKA_CONNECT_PLUGINS_DIR/postgres/protobuf-java-3.25.5.jar
COPY libs/postgresql-42.7.7.jar $KAFKA_CONNECT_PLUGINS_DIR/postgres/postgresql-42.7.7.jar

COPY libs/debezium-api-3.2.2.Final.jar $KAFKA_CONNECT_PLUGINS_DIR/postgres/debezium-api-3.2.2.Final.jar
COPY libs/debezium-common-3.2.2.Final.jar $KAFKA_CONNECT_PLUGINS_DIR/postgres/debezium-common-3.2.2.Final.jar
COPY libs/debezium-core-3.2.2.Final.jar $KAFKA_CONNECT_PLUGINS_DIR/postgres/debezium-core-3.2.2.Final.jar
COPY libs/debezium-openlineage-api-3.2.2.Final.jar $KAFKA_CONNECT_PLUGINS_DIR/postgres/debezium-openlineage-api-3.2.2.Final.jar

# Plugin postgres 2.7.x
#RUN mkdir -p $KAFKA_CONNECT_PLUGINS_DIR/postgres
#COPY libs/debezium-connector-postgres-2.7.2.Final.jar $KAFKA_CONNECT_PLUGINS_DIR/postgres/debezium-connector-postgres-2.7.2.Final.jar
#COPY libs/protobuf-java-3.25.2.jar $KAFKA_CONNECT_PLUGINS_DIR/postgres/protobuf-java-3.25.2.jar
#COPY libs/postgresql-42.6.1.jar $KAFKA_CONNECT_PLUGINS_DIR/postgres/postgresql-42.6.1.jar

RUN chown 1001:1001 -R $KAFKA_CONNECT_PLUGINS_DIR

USER 1001
