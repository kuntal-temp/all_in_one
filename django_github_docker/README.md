# Project Tree

```
├── .env.dev
├── .env.prod
├── .env.prod.db
├── .gitignore
├── app
│   ├── Dockerfile
│   ├── Dockerfile.prod
│   ├── entrypoint.prod.sh
│   ├── entrypoint.sh
│   ├── hello_django
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── manage.py
│   └── requirements.txt
├── docker-compose.prod.yml
├── docker-compose.yml
└── nginx
    ├── Dockerfile
    └── nginx.conf
```


To Build Image
```
docker-compose build
```

To Run the Container
```
docker-compose up -d
```

To Check docker log
```
docker-compose logs -f
```

To remove the volumes along with the containers and data will be lost
```
docker-compose down -v
```

To Build Container with a particuler .yml file
```
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.yml up -d --build
```

To delete all containers including its volumes use
```
docker rm -vf $(docker ps -a -q)
```

To delete all the images
```
docker rmi -f $(docker images -a -q)
```


To run migrations
```
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

To access database
```
docker-compose exec db psql --username=hello_django --dbname=hello_django_dev
```

To update permission .sh file
```
chmod +x entrypoint.sh
```

[For More like Nginx and Gunicon Setup](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)

[Deploy Your container in AWS](https://testdriven.io/blog/django-docker-https-aws/)

[Official Docker Guide On Django](https://docs.docker.com/compose/django/)
