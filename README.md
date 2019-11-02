# React Django GoodStuff

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) 

A [CookieCutter](https://github.com/cookiecutter/cookiecutter) template for modern, full-stack web applications.

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Features](#features)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
  * [Running Tests](#running-tests)
  * [Linting and Formatting](#linting-and-formatting)
  * [Development](#development)
  * [Shell Commands](#shell-commands)
  * [Python Extras](#python-extras)
  * [Deployment](#deployment)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

A major barrier to creating new projects is having to create the same basic infrastructure code over and over. Instead of recreating the same project structure over and over, use this polygot, _opinionated_ boilerplate to start new projects in a flash.

### Features

* Frontend powered by [React.js](https://reactjs.org/) ✨
* Python backend with [Django](https://djangoproject.com/) and [Django Rest Framework](https://www.django-rest-framework.org/) 🐍
* Container-first development- entire project built in Docker 🐳
* [Postgres](https://www.postgresql.org/) as the relational database 🐘
* [Redis](https://redis.io/) session and storage for _fast_ caching. 🚀
* [Django Allauth](https://github.com/pennersr/django-allauth) for easy social logins.
* Hot reloading development with Docker Compose, 12-factor inspired configuration, and more.

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

You will need GNU `make` and [CookieCutter](https://cookiecutter.readthedocs.io/en/latest/) installed on your system to use this template. Please note that usage on Windows (without WSL) is untested _and likely to have issues_.

### Installation
 
1. Use CookieCutter on the template:
```sh
cookiecutter gh:madelyneriksen/react-django-goodstuff
```
2. Start development!
```sh
make start
```

<!-- USAGE EXAMPLES -->
## Usage

### Docker First Philosophy 🐳

All dependencies of the project are bundled into Docker, with the final version of the project being a single Docker container. This is to maximize portability; on any machine with Docker you can build or even deploy the project effortlessly.

The implications on the project are that _all commands_, including tests, linting, and formatting, run via a Docker container. This ensures Docker remains a first-class citizen for the project and prevents discrepancies between development and production environments.

### Running Tests

Python tests are run with [Pytest](http://pytest.org/en/latest/) while React tests use [Jest](https://jestjs.io) and [Enzyme](https://airbnb.io/enzyme/).

While the tests themselves are run in Docker, for convenience there is a `make` target to run all tests:

```sh
make test
```

### Linting and Formatting

All Python code follows the [Black](https://github.com/psf/black) codestyle, while Javascript uses the [Airbnb Styleguide](https://github.com/airbnb/javascript).

You can check style and lint code with `make`, which wraps around a Docker command:

```sh
make lint
```

In cases where code can be auto-formatted (`eslint --fix` or `black`), you can use `make` to format the offending files:

```sh
make format
```

### Development

While creating webapps, it's handy to have hot module reloading to see changes as they are ready. Thankfully, you can do just that with this project on _both_ the Python and Javascript codebases, at the same time:

```sh
make start
```

Under the hood, this uses [Parcel's](https://parceljs.org) hot module reloading feature alongside [Gunicorn's](https://gunicorn.org/) `--reload` flag. Docker Compose binds the HMR websocket to the host, and the compiled javascript is collected and served by Gunicorn using [WhiteNoise](http://whitenoise.evans.io/en/stable/).

### Shell Commands

Sometimes, you just need a plain-old bash shell in your project. Maybe you need to run Django management commands, database migrations, or do some interactive debugging. You can open a shell with (you guessed it) `make`:

```sh
make shell
```

### Python Extras

#### Abstract Base Model

A `BaseModel` is included in `base.models` that uses a UUID field instead of an auto-incrementing integer. Oftentimes, this plays better with a single page application than an auto-incrementing ID does.

You can use the base model like you would the standard `models.Model` class in Django:

```python
class MyModel(BaseModel):
    """Just a regular model here, folks!"""
```

#### Redis Utilities

Interacting with Redis directly is often a requirement, so a couple utilities are included to do just that:


```python
from base.utils.redis import connection, RedisMixin

# connection() creates a singleton instance
redis = connection()

# You can also use a mixin to add a `.redis` property to any class

class MyClass(RedisMixin):
    pass

instance = MyClass()
instance.redis.ping()

# The redis instance is shared, and won't be duplicated.
assert instance.redis is redis
```

#### Testing Utilities

To make writing tests easier, [Pytest Django](https://pytest-django.readthedocs.io/en/latest/) is included. It adds useful fixtures for testing routes, integration tests on the database, and other helpers. Check it out!

#### URL-style configuration

Both Redis and Postgres connection settings are configured through environment variables that contain a URL string. This makes deployment of the application super straightforward.

```sh
# Some examples...
DATABASE_URL = postgres://username:password@host:5432/database
REDIS_URL = redis://redis:6379/0
```

#### Rest Framework

A standard integration with Django Rest Framework and Django Filters is included out of the box. An example route for `Users` is included in `base.api`, with the router stored in the main project folder.

If you want to use Graphql instead, try [Graphene Django](https://github.com/graphql-python/graphene-django). There is also a tutorial on using Graphql with Django [on my blog](https://www.madelyneriksen.com/graphql-django-tutorial) if you are interested in the details.

### Deployment

Thanks to Docker and WhiteNoise, deployment on _most_ cloud providers or any Kubernetes cluster is easy, and steps outside of the scope of this boilerplate.

However, you _should_ take care to set required environment variables:

- `DATABASE_URL` - Postgres uri string.
- `REDIS_URL` - Redis uri string.
- `SECRET_KEY` - Django secret key.

It might be nice to set these too:

- `ADMINS` - Add email addresses of the admin team.
- `EMAIL_BACKEND` - Configure your email solution.

Additionally, set `ALLOWED_HOSTS` in your settings file, and change the default site domain created by the Django sites framework. For more Django deployment information see the [official documentation.](https://docs.djangoproject.com/en/2.2/howto/deployment/)

## Contributing

Contributions are welcome, including bug, documentation, or feature requests. PRs/suggestions are also welcome and greatly appreciated!

<!-- LICENSE -->
## License

Distributed under terms of the MIT License.

<!-- CONTACT -->
## Contact

Madelyn Eriksen - [www.madelyneriksen.com/contact](https://www.madelyneriksen.com/contact)

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [audreyr's CookieCutter](https://github.com/cookiecutter/cookiecutter) for making this possible.
* [This README template](https://github.com/othneildrew/Best-README-Template) from othneildrew.
* The vibrant open-source community that enables projects like this. 🌈
