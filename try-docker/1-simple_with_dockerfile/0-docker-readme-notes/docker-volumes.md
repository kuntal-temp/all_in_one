# Docker Volumes


**List Of all Volumes**
```
    docker volume ls
```

**If you want your data need to be Persistent Data**
- Data Volumes
- Bind Mounts


**Try this to create Data Volumes**
Note: mysql store data **/var/lib/mysql** here so now if we can map that with our local then we can access our old data.
When we are removing docker container and image docker Volumes that is not removing 
because it is in our local and manage by docker. Volumes should be removed by the user only.

```
    docker run -d --name my-mysql -e MYSQL_ALLOW_EMPTY_PASSWORD=true -v mysql-db:/var/lib/mysql mysql
```

```
    >> docker volume inspect mysql-db

    Output:
    [
        {
            "CreatedAt": "2021-11-29T20:14:30+05:30",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/mysql-db/_data",
            "Name": "mysql-db",
            "Options": null,
            "Scope": "local"
        }
    ]
```

So, now when next time I will create a Mysql container we can use the old volume. 
Now our data is Persistent

```
    docker run -d --name my-mysql-2 -e MYSQL_ALLOW_EMPTY_PASSWORD=true -v mysql-db:/var/lib/mysql mysql
```

```
    Example:

    docker run -d --name my-psql -v psql-db:/var/lib/postgresql/data postgres
```


**Try this to create Bind Mounts**
- create one folder [mkdir myrepo && cd myrepo]
- touch index.html  [add some content here]

```
    - syntax: docker run -d --name my-nginx -p 8090:80 -v <your-local-dir>:/usr/share/nginx/html nginx

    - docker run -d --name my-nginx -p 8090:80 -v $(pwd):/usr/share/nginx/html nginx
        OR
    - docker run -d --name nginx -p 8090:80 -v /home/trynow/Desktop/myrepo/:/usr/share/nginx/html nginx

go and check http://127.0.0.1:8090/index.html
```

**Note**: With this below cmd, from docker bash we can access the local dir that we mapped [/home/trynow/Desktop/myrepo/]
Basically here we have mapped our local dir to within docker dir location

```
    docker exec -it my-nginx bash

    cd /usr/share/nginx/html   [you can see all local files and changes here]
```
