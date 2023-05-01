### docker-compose

Compose is a tool for defining and running multi-container Docker applications
Define the services that make up your app in docker-compose.yml so they can be 
run together in an isolated environment.


**It create network between multiple container, so that they can communicate**


**How To Build Image using docker-compose ?**
```
    - docker-compose up --build  [to build new image and run]

    - docker-compose up  [run the old build, if no build found then only create a new]
```


**How to lunch a Container in Background using compose file?**
```
    - docker-compose up -d
```


**How to stop a container which is running with compose file?**
```
    - docker-compose down
```


**This kind of output we can see when Start/Stop**
```
[Start]
Starting intro_to_docker_compose_postgres-db_1 ... done
Starting intro_to_docker_compose_flask-app_1   ... done

[Stop] Note: network also removed
Stopping intro_to_docker_compose_postgres-db_1 ... done
Stopping intro_to_docker_compose_flask-app_1   ... done
Removing intro_to_docker_compose_postgres-db_1 ... done
Removing intro_to_docker_compose_flask-app_1   ... done
Removing network intro_to_docker_compose_default
```
