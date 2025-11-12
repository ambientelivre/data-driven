![img.png](img.png)

Helm chart for https://github.com/apache/ranger

```
cd ranger/
helm upgrade --install ranger-local .  -n ranger-admin
```


![img_1.png](img_1.png)
admin/Rangeradmin1!


criar postgres-range.yaml  para postgres no mesmo namespace

## Caso for usar outro postgres mudar nos values
#### create a database in postgres
CREATE DATABASE ranger;
CREATE USER ranger WITH ENCRYPTED PASSWORD 'ranger';
GRANT ALL PRIVILEGES ON DATABASE rangerdb TO ranger;
