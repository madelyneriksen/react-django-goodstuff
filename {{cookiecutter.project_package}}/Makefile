FRONTEND_CONTAINER := {{ cookiecutter.project_package }}_app:latest
BACKEND_CONTAINER := {{ cookiecutter.project_package }}_api:latest
DEV_BACKEND_CONTAINER := {{ cookiecutter.project_package }}_api_dev

COMPOSE = docker-compose -f docker/docker-compose.yml
WAIT_FOR_DB = wait-for-it --service {{ cookiecutter.project_package }}_db:5432


.PHONY: build test lint migrations format


test: build
	docker-compose -f docker/docker-compose.test.yml \
	  run {{ cookiecutter.project_package }}_web \
	  /bin/bash -c \
	  "${WAIT_FOR_DB} && pytest"
	docker run --rm ${FRONTEND_CONTAINER} npm test

lint:
	docker run --rm ${FRONTEND_CONTAINER} npm run lint
	docker run --rm ${DEV_BACKEND_CONTAINER} black --exclude frontend --check .

shell:
	$(COMPOSE) run {{ cookiecutter.project_package }}_web /bin/bash

format:
	docker run --rm -v "${PWD}/frontend:/src/app" ${FRONTEND_CONTAINER} npm run format
	docker run --rm -v "${PWD}:/src/app" ${DEV_BACKEND_CONTAINER} black .

build:
	docker build -t ${FRONTEND_CONTAINER} -f docker/Dockerfile.app .
	docker build -t ${BACKEND_CONTAINER} -f docker/Dockerfile.api .
	docker build -t ${DEV_BACKEND_CONTAINER} \
	  --build-arg REQUIREMENTS=requirements.dev.txt \
	  -f docker/Dockerfile.api .

teardown:
	$(COMPOSE) down -v

start:
	$(COMPOSE) up
