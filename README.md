# Data Platform Case - Airflow on Kubernetes

Executando o Airflow no Kubernetes. Este repositório contém scripts para;
 
1) Executar um cluster K8s de vários nós na máquina local usando KinD
2) Dockerfile para suas dags do Airflow
3) Helm Chart para executar o Airflow no Kubernetes usando o Kubernetes Executor

## Requisitos

Kind: https://kind.sigs.k8s.io/docs/user/quick-start/#installation

kubectl: https://kubernetes.io/docs/tasks/tools

k9s: https://k9scli.io/topics/install

Docker: https://docs.docker.com/get-docker

Helm: https://helm.sh/docs/intro/install/

## Instruções de execução

1. Primeiro, crie um cluster Kubernets, executando o script bash `create_cluster_with_registry.sh` do diretório cluster/
2. Escreva sua própria dag e coloque-a dentro do diretório `airflow-dags/dags`. 
3. Em seguida, crie o arquivo docker, que está localizado dentro da pasta airflow-dags com o comando `docker build . -t case_pipeline:1.0.0`
4. Faça a tag da imagem com o host de registro do docker local `docker tag case_pipeline:1.0.0 localhost:5001/case_pipeline:1.0.0`
5. Envie a imagem do Airflow para o registro do docker local `docker push localhost:5001/case_pipeline:1.0.0`
6. Acesse a pasta airflow-task-image e execute o docker build `docker build . -t airflow_task:1.0.0`
7. Faça a tag da imagem com o host de registro do docker local `docker tag airflow_task:1.0.0 localhost:5001/airflow_task:1.0.0`
8. Envie a imagem do Airflow para o registro do docker local `docker push localhost:5001/airflow_task:1.0.0`
9. Aplique o Helm `helm upgrade --install airflow . --values values.yaml`