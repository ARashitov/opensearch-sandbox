# Apache Kafka sandbox

Project for investigation & personal experiments with Apache Kafka on Python

## 📦 Prerequisites

- Linux
- Docker & Docker-compose
- build-essentials package to run makefiles

## 💼 Management options

- to spin up docker container with kafka: `make kafka_run`
- to stop docker container with kafka: `make kafka_stop`

## 🐍 Python dependencies

1. Create python virtual environment
2. Activate environment
3. run: `make env_configure`
4. (optional): delete environment `make env_delete`
