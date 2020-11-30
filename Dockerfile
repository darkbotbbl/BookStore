FROM python:3.8.6-slim-buster

# environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# set work directory
WORKDIR /app

# install dependencies
COPY Pipfile Pipfile.lock /app/
RUN pip install pipenv 
RUN pipenv install --system

# copy the local code file
COPY . /app/