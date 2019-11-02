"""Post project generation hooks."""


import os
import subprocess


CONTAINER = "{{ cookiecutter.project_package }}_web"
DEV_CONTAINER_NAME = "{{ cookiecutter.project_package }}-dev:latest"
ENV = {"PWD": os.getcwd()}

DOCKER_BUILD = [
    "docker",
    "build",
    "-t",
    DEV_CONTAINER_NAME,
    "--build-arg",
    "REQUIREMENTS=requirements.dev.txt",
    "."
]

# Base container running command.
RUN_CONTAINER = ["docker-compose", "run", CONTAINER]

# Base management command.
MANAGE = [*RUN_CONTAINER, "python", "manage.py"]

# Postgres startup times require it to go up first in a compose setting.
DOCKER_COMPOSE_START_DB = [
    "docker-compose",
    "up",
    "-d",
    "{{ cookiecutter.project_package }}_db",
]
DOCKER_COMPOSE_MAKEMIGRATIONS = [*MANAGE, "makemigrations"]
DOCKER_COMPOSE_MIGRATE = [*MANAGE, "migrate"]
DOCKER_COMPOSE_TEST = [*RUN_CONTAINER, "pytest"]

# Generated migrations might not be formatted.
DOCKER_COMPOSE_FORMAT = [*RUN_CONTAINER, "black ."]


if __name__ == "__main__":
    run = lambda x: subprocess.run(x, env=ENV)
    run(DOCKER_BUILD)
    run(DOCKER_COMPOSE_START_DB)
    run(DOCKER_COMPOSE_MAKEMIGRATIONS)
    run(DOCKER_COMPOSE_MIGRATE)
    run(DOCKER_COMPOSE_TEST)
