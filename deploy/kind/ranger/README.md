![img.png](img.png)

Helm chart for https://github.com/apache/ranger

```
cd ranger/
helm upgrade --install ranger-local .  -n ranger-admin
```


![img_1.png](img_1.png)
admin/Rangeradmin1!


## create a database in postgres

CREATE DATABASE ranger;
CREATE USER ranger WITH ENCRYPTED PASSWORD 'ranger';
GRANT ALL PRIVILEGES ON DATABASE rangerdb TO ranger;
