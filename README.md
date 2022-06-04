# Fruit Service V3
Fruit Service v3 is a small REST API for demonstration purposes.

## Description
This is a REST API calling a MySQL server running on the same host.

## How to
To build the image have Docker Desktop (or Docker engine) running.

Then execute this command.
``` bash
docker build -t fruit-api-v3 .
```

To run it execute this command.
``` bash
docker run -dp 8000:8000 fruit-api-v3
```

To start Prometheus
``` bash
docker run -dp 9090:9090 -v ${PWD}/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus
```