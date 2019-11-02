"""Post project generation hooks."""


import os
import subprocess


ENV = {"PWD": os.getcwd()}

BUILD = ["make", "build"]
CREATE = ["docker-compose", "up", "--no-start"]


if __name__ == "__main__":
    run = lambda x: subprocess.run(x, env=ENV)
    run(BUILD)
    run(CREATE)
