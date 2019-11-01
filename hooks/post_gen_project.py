"""Post project generation hooks."""


import os
from subprocess import run


PROD_CONTAINER = "{{ cookiecutter.project_package }}:latest"
DEV_CONTAINER = "{{ cookiecutter.project_package }}-dev:latest"
DOCKER_BUILD = ["docker", "build", "-t", DEV_CONTAINER, "."]
DOCKER_MIGRATE = [
    "docker",
    "run",
    "-v",
    f"{os.getcwd()}:/src/app",
    DEV_CONTAINER,
    "python",
    "manage.py",
    "makemigrations",
]


if __name__ == "__main__":
    run(DOCKER_BUILD)
    run(DOCKER_MIGRATE)
