#!/bin/bash

docker rm backend nginx frontend pg_admin

docker rmi distribution_of_the_budgeting_system-backend
docker rmi distribution_of_the_budgeting_system-nginx
docker rmi distribution_of_the_budgeting_system-frontend

docker compose -f docker-compose.yml up
