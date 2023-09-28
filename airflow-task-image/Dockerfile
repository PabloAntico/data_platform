FROM ubuntu:22.04

# Adicionando rótulos à imagem para ajudar a identificá-la no futuro.
LABEL maintainer="Pablo Antico"
LABEL github="https://github.com/PabloAntico"
LABEL docker.module="airflow-task-image"
LABEL docker.component="airflow-task-image"

USER root
RUN apt-get update
RUN apt-get -y install python3-pip \
    && pip install boto3 \
    && pip install pandas

COPY . .