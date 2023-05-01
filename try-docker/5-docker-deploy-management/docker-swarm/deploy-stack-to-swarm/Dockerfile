# pull official base image
FROM python:3.8.2-alpine

# set work directory
WORKDIR /usr/src

# minimizing rebuild time using cache
COPY ./requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project [taking cache help here]
COPY ./ ./

# to run the code.py
ENTRYPOINT ["python"]
CMD ["code_file.py"]
