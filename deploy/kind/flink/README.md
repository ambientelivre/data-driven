kubectl apply -f https://github.com/jetstack/cert-manager/releases/download/v1.15.3/cert-manager.yaml     —-> deploy cert-manager on k8s

helm repo add flink-operator-repo https://downloads.apache.org/flink/flink-
kubernetes-operator-1.9.0    —-> add operator repo

helm install flink-kubernetes-operator flink-operator-repo/flink-kubernetes-operator  →install operator


READ: https://medium.com/@tomkrol_39593/kafka-producer-with-apache-flink-in-a-few-steps-8f0a4f50bcfe
