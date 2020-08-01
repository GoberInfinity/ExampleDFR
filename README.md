# ExampleDFR

Example of Django REST framework.

## Prerequisites

- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Development

The project uses postgresql as a database and the server is running gunicorn with 5 workers configured as async to be to handle more than one request and not be bounded to that request until it's finished

#### Run the project

1. You will need to setup the following environment variables in your system in order to be able to upload the csv file to your own bucket:

   - AWS_ACCESS_KEY_ID
   - AWS_SECRET_ACCESS_KEY
   - AWS_STORAGE_BUCKET_NAME
   - AWS_SESSION_TOKEN

     **Note**: The AWS_SESSION_TOKEN is optional, set it if your aws configuration needs it

1. Start the dev server for local development:

   ```bash
   sudo -E docker-compose up
   ```

#### Endpoints

You can access the api using the following urls:

| Url                              | Description                                                    |
| -------------------------------- | -------------------------------------------------------------- |
| localhost:8000/api/v1/users/     | Creates users into Django Users Models                         |
| localhost:8000/api/v1/users/:id/ | Detail about an user                                           |
| localhost:8000/api/v1/upload/    | Uploads a csv file to s3 and puts all the info in the database |
| localhost:8000/api/v1/data/      | Retrieves all information of all csv files from the database   |

**Note**: If you would like to see more information about each endpoint and how it works check the _documentation_ section

#### Testing

All the enpoinds of the project were tested, to run all the tests:

```bash
docker-compose run --rm web ./manage.py test api.users.test.test_views
docker-compose run --rm web ./manage.py test api.users.test.test_serializers
```

#### Documentation

The documentation was created using [MkDocs](https://www.mkdocs.org/) if you want to know how to use the api you can access to the documentation using `localhost:8001`

#### Quality Code

The code was cleaned up using [flake8](https://flake8.pycqa.org/en/latest/) if you want to check any potential errors run:

```bash
docker-compose run --rm web flake8 .
```

#### CI

The project is ready to run in travis CI
