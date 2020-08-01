# ExampleDFR

Example of Django REST framework. Check out the project's [documentation](http://GoberInfinity.github.io/ExampleDFR/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)

# Initialize the project

Start the dev server for local development:

```bash
docker-compose up
```

Create a superuser to login to the admin:

```bash
docker-compose run --rm web ./manage.py createsuperuser
```
