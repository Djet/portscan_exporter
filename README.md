# Portscan exporter

[![Docker Pulls](https://img.shields.io/docker/pulls/djet/portscan-exporter.svg?maxAge=604800)][hub]

The portscan exporter scans for open ports

## Running this software

### Config file

```
server_port: 8000
update_time: 600
server_list:
 - 8.8.8.8
 - 140.82.121.3
```

### Using the docker image

    docker run --rm -d -p 9115:9115 --name portscan_exporter -v `pwd`:/config djet/portscan-exporter:master --config.file=/config/portscan.yml

### Checking the results

Visiting [http://localhost:9115/probe?target=google.com&module=http_2xx](http://localhost:9115/probe?target=google.com&module=http_2xx)
will return metrics for a HTTP probe against google.com. The `probe_success`
metric indicates if the probe succeeded. Adding a `debug=true` parameter
will return debug information for that probe.

## Building the software

### Building with Docker

After a successful local build:

    docker build -t portscan_exporter .


[hub]: https://hub.docker.com/r/djet/portscan-exporter/
