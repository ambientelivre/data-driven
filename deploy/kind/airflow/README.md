## Airflow

### K8S - Kind

#### Helm
https://airflow.apache.org/docs/helm-chart/stable/index.html

```shell
helm repo add apache-airflow https://airflow.apache.org
helm upgrade --install airflow apache-airflow/airflow --namespace airflow --create-namespace
```

## upgrade chart 

```shell
helm upgrade airflow apache-airflow/airflow --namespace airflow
```

https://airflow.apache.org/docs/helm-chart/stable/parameters-ref.html
https://artifacthub.io/packages/helm/apache-airflow/airflow
https://github.com/apache/airflow/tree/main/chart

```shell
wget https://raw.githubusercontent.com/apache/airflow/refs/heads/main/chart/values.yaml
```


### Update de values 

```shell
helm show values apache-airflow/airflow > values.yaml
helm upgrade --install airflow apache-airflow/airflow --namespace airflow -f values.yaml
```

#### Unnistall
```shell
helm delete airflow --namespace airflow
helm uninstall airflow -n airflow
kubectl delete all --all -n airflow
kubectl delete pvc --all -n airflow
kubectl delete secret --all -n airflow
kubectl delete configmap --all -n airflow
kubectl delete job --all -n airflow
kubectl delete ns airflow

```


#####  Installing the Chart with Argo CD, Flux, Rancher or Terraform

createUserJob:
  useHelmHooks: false
  applyCustomEnv: false
migrateDatabaseJob:
  useHelmHooks: false
  applyCustomEnv: false
  
##### ArgoCD
 
 migrateDatabaseJob:
    jobAnnotations:
        "argocd.argoproj.io/hook": Sync 
  
  
  Your release is named airflow.
You can now access your dashboard(s) by executing the following command(s) and visiting the corresponding port at localhost in your browser:
Airflow API Server:     kubectl port-forward svc/airflow-api-server 8080:8080 --namespace airflow
Default Webserver (Airflow UI) Login credentials:
    username: admin
    password: admin
Default Postgres connection credentials:
    username: postgres
    password: postgres
    port: 5432

You can get Fernet Key value by running the following:

    echo Fernet Key: $(kubectl get secret --namespace airflow airflow-fernet-key -o jsonpath="{.data.fernet-key}" | base64 --decode)

###########################################################
###  WARNING: You should set a static webserver secret key  #
###########################################################

You are using a dynamically generated webserver secret key, which can lead to
unnecessary restarts of your Airflow components.

Information on how to set a static webserver secret key can be found here:


