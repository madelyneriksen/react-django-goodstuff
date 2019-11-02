FRONTEND_CONTAINER := {{ cookiecutter.project_package }}-app:latest
BACKEND_CONTAINER := {{ cookiecutter.project_package }}-api:latest


.PHONY: test


test: build
	docker-compose exec {{ cookiecutter.project_package }} pytest --pdb
	docker run --rm ${FRONTEND_CONTAINER} npm test

build:
	docker build -t ${FRONTEND_CONTAINER} -f docker/Dockerfile.app .
	docker build -t ${BACKEND_CONTAINER} -f docker/Dockerfile.api .
