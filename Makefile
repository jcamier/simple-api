.PHONY: all build up down sh test lint

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

lint:
	docker-compose run --rm app sh -c "flake8"

sh:
	docker-compose run --rm app sh
