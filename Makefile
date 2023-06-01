init: stop pull build

up:
	docker-compose up -d
stop:
	docker-compose down --remove-orphans
build:
	docker-compose up -d --build
pull:
	docker-compose pull