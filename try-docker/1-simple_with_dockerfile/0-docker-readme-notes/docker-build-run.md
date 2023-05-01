# Docker Build & Run


**To test Docker is running or not**
```
    docker run hello-world
```

**How to Overriding Default Command?**
busybox: [Dockefile]
    FROM scratch
    ADD busybox.tar.xz /
    CMD ["sh"]

```
    syntax: docker run <imgae-name> <command-to-override>
    - docker run busybox echo hey there!
    - docker run busybox ls
    - docker run busybox ping www.google.com
```

**Build & Run image with Name**
```
    docker run --name <my-given-name> redis
```

**To build your image and tagging**
```
    - docker build .   [this cmd will return a random Build ID]
    - docker build /Desktop/my-folder
    - docker build -t username/project-name:version-name .  [tagging during creation of image]
```

**How To Run the Image and run from tag**
```
    - docker run <build-id>
    - docker run username/project-name:version-name
```



**Build and run using docker-compose**
```
    - docker-compose build [only build]
    - docker-compose up  [build from cache]

    - docker-compose up --build  [build from uptodate and run]

    - docker-compose build && docker-compose up  [build + run]
```


**Uses of Multi Dockerfile and Multi docker-compose files**
- specific Dockerfile
```
    - synatx: docker build -f <Dockerfile-name> .

    - docker build -f Dockerfile.dev .  [use for dev env]
```

- specific docker-compose.yml
```
    To Build Container with a particuler .yml file

    - docker-compose -f docker-compose.yml up --build
    
    - docker-compose -f docker-compose.prod.yml up --build
```

**How to run a container in Background ?**
```
    - syntax: docker run -d <build-id>

    - docker run -d redis [Example to run redis in background]
```

**How to execute a command within a Running container?**

- start an interactive shell with running a new container
```
    syntax: docker run -it <image-name>

    - docker run -it ubuntu
```

- **start an interactive shell from already running container**
```
Let's assume redis-server is running I want to use redis cli

    syntax: docker exec -it <container-id> <command>

    - docker exec -it <container-id> redis-cli   [Example]
    - docker exec -it <container-id> sh          [shell access to execute command]
```

**Check docker Log for a container**
```
    docker log <build-id>
```

**Details Info for a container**
```
    - docker history <container-id>
    - docker top <container-id>  [process list of container]
    - docker inspect <container-id>  [response json in deatils]
    - docker stats or - docker stats <container-id>  [Live stats monitering]
```

--------------------------------------------------------------------------------

**docker run** = docker create + docker start

To create a Container
```
    docker create <image-name>
```

To start a Container
```
    docker start <container-id>
```

#### Example
```
    - docker create hello-world --> will retun a <unque-id>
    - docker start -a <unque-id>
```

This **-a** is basically attach container with our terminal

If some forget to use **-a** the also they check the log within the container using below command
```
    docker log <unque-id>
```


--------------------------------------------------------------------------------------
- **Entrypoint and CMD difference**

The ENTRYPOINT instruction works very similarly to CMD in that it is used to specify the command executed when the container is started. However, where it differs is that ENTRYPOINT doesn't allow you to override the command.

```
    ENTRYPOINT ["python"]
    CMD ["code_file.py"]
```

```
    ENTRYPOINT ["python", "code_file.py"]
    CMD ["python", "code_file.py"]
```
