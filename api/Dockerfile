# base image
FROM python:3.10-slim-bullseye

# set environment variables
ENV PYTHONUNBUFFERED 1

# set directory
WORKDIR /api

# install dependencies and add application
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy --ignore-pipfile
COPY . ./

# run the app
CMD ["supervisord", "-c", "supervisord.conf"]
