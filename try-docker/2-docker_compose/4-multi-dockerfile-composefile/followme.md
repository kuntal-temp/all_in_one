### Uses of Multi Dockerfile and Multi docker-compose files


When we have multiple dockerfile to use for different env the we can use the bellow command
```
    - synatx: docker build -f <Dockerfile-name> .

    - docker build -f Dockerfile.dev .  [use for dev env]
```

**Build & Run Container using a specific docker-compose file**
```
    To Build Container with a particuler .yml file

    - docker-compose -f docker-compose.yml up --build
    
    - docker-compose -f docker-compose.prod.yml up --build
```


**To build from specific Dockerfiles using Docker Compose**
```
    - docker-compose up --build
```


### Explain code
```
    build:
      context: .
      dockerfile: Dockerfile.dev
```
this means go to current dir and find Dockerfile.dev and then build with that
