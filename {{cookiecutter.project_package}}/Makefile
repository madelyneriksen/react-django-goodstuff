FRONTEND_CONTAINER := {{ cookiecutter.project_package }}_app:latest
BACKEND_CONTAINER := {{ cookiecutter.project_package }}_api:latest
DEV_BACKEND_CONTAINER := {{ cookiecutter.project_package }}_api_dev


.PHONY: build test lint migrations format


test:
	docker-compose run {{ cookiecutter.project_package }}_web /bin/bash -c "pytest && black --check ."
	docker run --rm ${FRONTEND_CONTAINER} npm test

lint:
	docker run --rm ${FRONTEND_CONTAINER} npm run lint

migrations:
	docker-compose run {{ cookiecutter.project_package }}_web python manage.py makemigrations

format:
	cd frontend && npm run format
	black .

build:
	docker build -t ${FRONTEND_CONTAINER} -f docker/Dockerfile.app .
	docker build -t ${BACKEND_CONTAINER} -f docker/Dockerfile.api .
	docker build -t ${DEV_BACKEND_CONTAINER} \
	  --build-arg REQUIREMENTS=requirements.dev.txt \
	  -f docker/Dockerfile.api .
