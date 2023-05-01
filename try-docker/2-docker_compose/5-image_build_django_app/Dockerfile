# pull official base image
FROM python:3.9-alpine

# set work directory
WORKDIR /usr/src

# copy and install requirements
COPY ./requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy env for local config
COPY ./.env ./
COPY ./ ./

# ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]  [when to run using Dockerfile]
