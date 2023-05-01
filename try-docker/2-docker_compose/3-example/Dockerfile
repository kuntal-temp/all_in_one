# pull official base image
FROM python:3.9-alpine

# set work directory
WORKDIR /usr/src

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# minimizing rebuild time using cache
COPY ./requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project [taking cache help here]
COPY ./ ./

# to run the code.py
ENTRYPOINT ["python"]
CMD ["test_code.py"]
