# install trino k8s
##### docs samples https://github.com/trinodb/charts/tree/main/tests/trino
##### https://artifacthub.io/packages/helm/trino/trino

helm repo add trino https://trinodb.github.io/charts

git clone https://github.com/ambientelivre/data-driven.git
cd  data-driven/deploy/kind/trino

kubectl apply -f trino-ns.yaml

helm install trino-cluster trino/trino --namespace trino
helm upgrade --install -f values.yaml trino-cluster trino/trino --namespace trino

kubectl get all -n trino

kubectl get svc -n trino


kubectl port-forward svc/trino-cluster-trino 8080:8080 -n trino

kubectl get pods -n trino
kubectl exec -it trino-cluster-trino-coordinator-8c65fb6bc-l9bg2  -n trino -- trino

select count(*) from tpch.tiny.nation;

## Criando uma nova senha (no deploy esta admin/sejalivre) 
# docs https://trino.io/docs/current/security/password-file.html#file-format
htpasswd -B -C 10 -c password.db admin
informar a senha : sejalivre
cat password.db

mude em values.yaml
auth:
  passwordAuth: "admin:$2y$10$yKmUAEpKMERziU9uUPvvS.etPlvzncR3LVIfx.a9TY6yP1xd/x1ZK"


## certificado autogerado
https://trino.io/docs/current/security/internal-communication.html?utm_source=chatgpt.com

## Erros no chats ele não apaga esta linha sempre vem default removemo com post-renderer
###### op charts sempre adicionava a linha abaixo gerandop erros
###### server.https.keystore.path=

## crieado post-renderer

nano remove-keystore.sh

#!/bin/bash
# Remove a linha "http-server.https.keystore.path" do ConfigMap do Trino
sed '/http-server\.https\.keystore\.path=/d'

chmod +x remove-keystore.sh


helm upgrade --install trino-cluster trino/trino \
  -f values.yaml \
  --namespace trino \
  --post-renderer ./remove-keystore.sh

## exemplos pos corrigido

kubectl exec -it trino-cluster-trino-coordinator-6bd88b54b8-sxlbp -n trino -- cat /etc/trino/config.properties 
coordinator=true
node-scheduler.include-coordinator=false
http-server.http.port=8080
query.max-memory=4GB
query.max-memory-per-node=1GB
discovery.uri=http://localhost:8080
http-server.authentication.type=PASSWORD
internal-communication.shared-secret=xFht55VmLbEgGucdUEZnIH/Yn+/9zIEZzeVDGLFMMpo=
http-server.process-forwarded=true
internal-communication.https.required=true
http-server.https.enabled=true
http-server.https.port=8443



kubectl -n trino port-forward svc/trino-cluster-trino 8443:8443

## testando

kubectl exec -it trino-cluster-trino-coordinator-548d7bd977-n4l28 -n trino -- trino --server https://localhost:8443 --user admin --password --insecure

