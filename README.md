# Docker Nginx + Let's Encrypt

Example of a docker compose config for containers with HTTPS.

## Introduction

This repository contains reference docker-compose file for a variety of [nginx-proxy](https://github.com/nginx-proxy/nginx-proxy) with [acme-companion](https://github.com/nginx-proxy/acme-companion) (Let's Encrypt) setup.

## Requirement

1. Install [Docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04)
2. Install [Docker Compose](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04)
3. Create a docker network called `nginx-proxy`

> All the docker-compose file assume the existence of a docker network called `nginx-proxy`. Create it with the following command before starting the containers.

```bash
docker network create nginx-proxy
```

## Useful commands

```bash
docker-compose up -d
```

```bash
docker-compose down
```

```bash
docker exec nginx-proxy-acme /app/cert_status
```

```bash
docker-compose logs -f
```

## Links

- [nginx-proxy](https://github.com/nginx-proxy/nginx-proxy)
- [acme-companion](https://github.com/nginx-proxy/acme-companion)
- [Install Docker - Digital Ocean tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04)
- [Install Docker Compose - Digital Ocean tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04)
- [Docker Compose Releases](https://github.com/docker/compose/releases)
