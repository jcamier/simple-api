.PHONY: all build up down prune test sh

all: test lint up

build:
	docker-compose build

up-service:
	docker-compose up

down:
	docker-compose down --remove-orphans

prune:
	docker image prune -f
	docker container prune -f

up: prune down up-service

test:
	docker-compose run --rm app pytest tests/

sh:
	docker-compose run --rm app sh
