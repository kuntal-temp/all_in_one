# pull official base image
FROM python:3.9-alpine

# set work directory
WORKDIR /usr/src

# minimizing rebuild time using cache
COPY ./requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project [taking cache help here]
COPY ./ ./
