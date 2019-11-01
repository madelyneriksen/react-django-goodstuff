"""Post project generation hooks."""


import os
import subprocess


CONTAINER = "{{ cookiecutter.project_package }}_web"
DEV_CONTAINER_NAME = "{{ cookiecutter.project_package }}-dev:latest"
DOCKER_BUILD = ["docker", "build", "-t", DEV_CONTAINER_NAME, "."]
ENV = {"PWD": os.getcwd()}

# Postgres startup times require it to go up first in a compose setting.
DOCKER_COMPOSE_START_DB = [
    "docker-compose",
    "up",
    "-d",
    "{{ cookiecutter.project_package }}_db",
]

DOCKER_COMPOSE_MAKEMIGRATIONS = [
    "docker-compose",
    "run",
    CONTAINER,
    "python",
    "manage.py",
    "makemigrations",
]

DOCKER_COMPOSE_MIGRATE = [
    "docker-compose",
    "run",
    CONTAINER,
    "python",
    "manage.py",
    "migrate",
]


if __name__ == "__main__":
    run = lambda x: subprocess.run(x, env=ENV)
    run(DOCKER_BUILD)
    run(DOCKER_COMPOSE_START_DB)
    run(DOCKER_COMPOSE_MAKEMIGRATIONS)
    run(DOCKER_COMPOSE_MIGRATE)
