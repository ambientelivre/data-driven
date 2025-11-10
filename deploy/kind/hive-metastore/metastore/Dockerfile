FROM apache/hive:4.0.0

COPY libs /opt/hadoop/share/hadoop/common/lib/
COPY libs /opt/hive/lib/

COPY conf/core-site.xml /opt/hive/conf
COPY conf/hive-site.xml /opt/hive/conf
COPY conf/metastore-site.xml /opt/hive/conf
