# Portscan exporter

[![Docker Pulls](https://img.shields.io/docker/pulls/djet/portscan_exporter.svg?maxAge=604800)][hub]

The portscan exporter scans for open ports

## Running this software

### Config file

```
server_port: 9115
update_time: 600
server_list:
 - 8.8.8.8
 - 140.82.121.3
```

### Using the docker image
    docker run --rm -d -p 9115:9115 --name portscan_exporter -v $(pwd):/config djet/portscan_exporter --config /config/portscan.yml

### Using the docker compose

```
version: '3'

services:
  portscan_exporter:
    image: djet/portscan_exporter:latest
    volumes:
      - ./config:/config
    command:
      - '--config=/config/portscan_exporter.yml'
    ports:
      - 9115:9115
    restart: always

```

## Building the software

### Building with Docker

After a successful local build:

    docker build -t portscan_exporter .


[hub]: https://hub.docker.com/r/djet/portscan_exporter/
