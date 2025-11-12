

helm repo add apache-ranger https://ahmetfurkandemir.github.io/charts/demir-open-source/apache-ranger/



helm upgrade --install apache-ranger apache-ranger/apache-ranger --version 0.1.0 -n apache-ranger --create-namespace

