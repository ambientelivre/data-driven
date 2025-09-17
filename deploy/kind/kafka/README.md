



## Permissões para o user KafkaConnect/debezium conectar no Postgres

Este cenario preve um database no postgres chamado sample_data com uma tabela 
chamada users


´´´sql
GRANT CONNECT ON DATABASE sample_data TO usr_kafka;
ALTER ROLE usr_kafka WITH REPLICATION;
GRANT USAGE ON SCHEMA public TO usr_kafka;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO usr_kafka;
GRANT SELECT ON ALL SEQUENCES IN SCHEMA public TO usr_kafka;
´´´
