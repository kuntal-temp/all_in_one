### Quick-start development settings - unsuitable for production
```
    See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/
```


### install psycopg2 dependencies
```
    - Update the Dockerfile
    
    RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
```

### Notes
If you want to run the nunserver command on Dockerfile
then
```
    ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
    
    OR

    ENTRYPOINT ["python"]
    CMD ["manage.py", "runserver", "0.0.0.0:8000"]
```

If you want to run the nunserver command on docker-compose file
then **Recomended to Run Here**
```
    my-django-docker-app:
        build: ./
        command: python manage.py runserver 0.0.0.0:8000
        ports:
        - 8000:8000
```

**Uses of depends_on?**
```
    services:
        web:
            build: ./
            depends_on:
                - db
                - redis
```
**Note:** It will start services in dependency order. In the following example, db and redis will be started before web.

**Note:** depends_on will not wait for db and redis to be “ready” before starting web - only until they have been started


