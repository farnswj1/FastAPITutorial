# FastAPI Tutorial
This is a containerized FastAPI tutorial.

## Setup
The project uses the following:
- Python 3.10
- FastAPI
- PostgreSQL 14
- Redis 7
- Nginx 1.21
- Docker
- Docker Compose

For additional information on project specifications, see the ```Pipfile```.

### Environment
In the ```api/``` directory, create a ```.env``` file
that contains the following environment variables:
```
ALLOWED_HOSTS=localhost 127.0.0.1
CORS_ALLOW_ORIGIN_REGEX=^https?://(localhost|127\.0\.0\.1)$
DATABASE_URL=postgresql://postgres:password@postgres:5432/fastapi_tutorial
REDIS_URL=redis://redis:6379
```

## Building
The project uses Docker. Ensure Docker and Docker Compose are installed before continuing.

To build, run ```docker-compose build```

## Running
To run the web app, run ```docker-compose up -d```, then 
go to http://localhost/docs using your web browser.
