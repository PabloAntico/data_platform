#Building Cluster Kubernetes
bash ./cluster/create_cluster_with_registry.sh

#Building the Core Image to run Airflow
docker build ./airflow-dags -t case_pipeline:1.0.0
docker tag docker.io/library/case_pipeline:1.0.0 localhost:5001/case_pipeline:1.0.0
docker push localhost:5001/case_pipeline:1.0.0

#Building the Task Image to run in PODs
docker build ./airflow-task-image -t airflow_task:1.0.0
docker tag docker.io/library/airflow_task:1.0.0 localhost:5001/airflow_task:1.0.0
docker push localhost:5001/airflow_task:1.0.0

#Building Airflow Env in Kubernetes Cluster
cd ./helm-chart/ && helm upgrade --install airflow . --namespace default --values values.yaml
