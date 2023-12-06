#!/bin/bash

docker stop buildx_buildkit_default

docker rm buildx_buildkit_defaultn

docker rmi buildx-stable-1

# docker compose -f docker-compose.production.yml up
