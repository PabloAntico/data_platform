FROM apache/airflow:2.3.3-python3.8 as build

# Adicionando rótulos à imagem para ajudar a identificá-la no futuro.
LABEL maintainer="Pablo Antico"
LABEL github="https://github.com/PabloAntico"
LABEL docker.module="airflow"
LABEL docker.component="airflow"
LABEL docker.airflow.version="2.3.3"

USER root
RUN export ACCEPT_EULA=Y && \
    apt-get autoremove -yqq --purge && \
    apt-get clean && \
    apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y gcc && \
    apt-get -y install default-libmysqlclient-dev && \
    apt-get -y install pkg-config && \
    sudo pip install mysqlclient

USER airflow

# Abaixo exemplo oficial da Airflow: https://airflow.apache.org/docs/docker-stack/build.html#example-when-you-want-to-embed-dags

# Este comando irá copiar a pasta DAGS para dentro do seu cluster.
# Ponto importante a ser observado aqui é que não consegui efetuar o BIND da pasta local para o pod, assim fazendo com que a pasta de DAGs fosse gerenciada enquanto o cluster está de pé.
COPY --chown=airflow:root ../dags  /opt/airflow/dags