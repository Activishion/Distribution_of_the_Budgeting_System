#!/bin/bash

docker stop buildx_buildkit_default

docker rm buildx_buildkit_defaultn

docker rmi buildx-stable-1

# docker compose -f docker-compose.production.yml up

DOCKER_BUILDKIT=0 docker-compose -f docker-compose.production.yml up
# создание связки образов докер-компоуз



docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker rmi $(docker images -a -q)

docker volume ls
docker volume prune
