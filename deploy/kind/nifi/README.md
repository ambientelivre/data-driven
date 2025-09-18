## Nifi

## Operator Nifi

https://konpyutaika.github.io

# Install the CustomResourceDefinitions and cert-manager itself

wget https://github.com/jetstack/cert-manager/releases/download/v1.17.2/cert-manager.yaml


kubectl apply -f cert-manager.yaml

```ssh
wget https://raw.githubusercontent.com/konpyutaika/nifikop/master/config/crd/bases/nifi.konpyutaika.com_nificlusters.yaml
wget https://raw.githubusercontent.com/konpyutaika/nifikop/master/config/crd/bases/nifi.konpyutaika.com_nifiusers.yaml
wget https://raw.githubusercontent.com/konpyutaika/nifikop/master/config/crd/bases/nifi.konpyutaika.com_nifiusergroups.yaml
wget https://raw.githubusercontent.com/konpyutaika/nifikop/master/config/crd/bases/nifi.konpyutaika.com_nifidataflows.yaml
wget https://raw.githubusercontent.com/konpyutaika/nifikop/master/config/crd/bases/nifi.konpyutaika.com_nifiparametercontexts.yaml
wget https://raw.githubusercontent.com/konpyutaika/nifikop/master/config/crd/bases/nifi.konpyutaika.com_nifiregistryclients.yaml
wget https://raw.githubusercontent.com/konpyutaika/nifikop/master/config/crd/bases/nifi.konpyutaika.com_nifinodegroupautoscalers.yaml
wget https://raw.githubusercontent.com/konpyutaika/nifikop/master/config/crd/bases/nifi.konpyutaika.com_nificonnections.yaml
wget https://raw.githubusercontent.com/konpyutaika/nifikop/master/config/crd/bases/nifi.konpyutaika.com_nifiresources.yaml

kubectl apply -f nifi.konpyutaika.com_nificlusters.yaml
kubectl apply -f nifi.konpyutaika.com_nifiusers.yaml
kubectl apply -f nifi.konpyutaika.com_nifiusergroups.yaml
kubectl apply -f nifi.konpyutaika.com_nifidataflows.yaml
kubectl apply -f nifi.konpyutaika.com_nifiparametercontexts.yaml
kubectl apply -f nifi.konpyutaika.com_nifiregistryclients.yaml
kubectl apply -f nifi.konpyutaika.com_nifinodegroupautoscalers.yaml
kubectl apply -f nifi.konpyutaika.com_nificonnections.yaml
kubectl apply -f nifi.konpyutaika.com_nifiresources.yaml
```

kubectl create ns nifi


helm install nifikop \
    oci://ghcr.io/konpyutaika/helm-charts/nifikop \
    --namespace=nifi \
    --version 1.14.2 \
    --set image.tag=v1.14.2-release \
    --set resources.requests.memory=256Mi \
    --set resources.requests.cpu=250m \
    --set resources.limits.memory=256Mi \
    --set resources.limits.cpu=250m \
    --set namespaces={"nifi"}
    
kubectl --namespace nifi get pods -l "release=nifikop"    

    
## Deploy Cluster usando Operator
https://konpyutaika.github.io/nifikop/docs/3_manage_nifi/1_manage_clusters/1_deploy_cluster/1_quick_start

*** Analisar trocar imagem****
 
helm install zookeeper oci://registry-1.docker.io/bitnamicharts/zookeeper \
    --namespace=zookeeper \
    --set resources.requests.memory=256Mi \
    --set resources.requests.cpu=250m \
    --set resources.limits.memory=256Mi \
    --set resources.limits.cpu=250m \
    --set global.storageClass=standard \
    --set networkPolicy.enabled=true \
    --set replicaCount=3 \
    --create-namespace
    

kubectl apply -f service-account.yaml

wget https://raw.githubusercontent.com/konpyutaika/nifikop/refs/heads/master/config/samples/simplenificluster.yaml

kubectl create -n nifi -f simplenificluster.yaml

#kubectl delete -n nifi -f simplenificluster.yaml

## desabilitado temporariamente
  #oneNifiNodePerNode: true

## atencao aos numero de CPU para o RANCHER


kubectl get events -n nifi --sort-by=.metadata.creationTimestamp 



kubectl port-forward svc/driver-ip 8080:8080 -n nifi

## Versao 2.5 cluster Nifi

kubectl delete ns nifi
kubectl create ns nifikop

wget https://raw.githubusercontent.com/konpyutaika/nifikop/refs/heads/master/config/samples/http_nificluster.yaml


kubectl apply -n nifikop -f http_nificluster.yaml







  
  
   
    
    
    















    
    
## plugisn opcionais
 kubectl-nifikop    ????
     








    

