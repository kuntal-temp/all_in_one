# deploy django project on swarm


To run in local
```
    docker-compose -f docker-compose.local.yml up --build

    docker-compose -f docker-compose.local.yml down
```


To build my image
```
    docker build -t kuntalsamantadocker/kuntal-docker-django . 
```

To push the image to docker hub
```
    docker push kuntalsamantadocker/kuntal-docker-django
```

Now try to deploy your image into Swarm
```
    docker stack deploy --compose-file docker-compose.yml my-swarm-stack-demo
```

Go Test
```
    http://127.0.0.1:9000/
```

How to check the log for any running services?
```
    docker service logs <service name/id>      # docker service ls [get the name or id from here]
```

To remove from stack
```
    docker stack rm my-swarm-stack-demo
```

----------
List of services for that stack
```
    > docker stack services my-swarm-stack-demo

    ID             NAME                                       MODE         REPLICAS   IMAGE                                             PORTS
    bm32bdqu5muc   my-swarm-stack-demo_celery                 replicated   1/1        kuntalsamantadocker/kuntal-docker-django:latest   
    to198fswl8oi   my-swarm-stack-demo_celery-beat            replicated   1/1        kuntalsamantadocker/kuntal-docker-django:latest   
    eupqlfwpxedl   my-swarm-stack-demo_my-django-docker-app   replicated   2/2        kuntalsamantadocker/kuntal-docker-django:latest   *:9000->8000/tcp
    qhfg20mwogdc   my-swarm-stack-demo_my-unit-test           replicated   0/1        kuntalsamantadocker/kuntal-docker-django:latest   
    xmkdc327t85w   my-swarm-stack-demo_redis                  replicated   1/1        redis:alpine                                      
    5g1hqo4eg4cs   my-swarm-stack-demo_run-migrate            replicated   0/1        kuntalsamantadocker/kuntal-docker-django:latest
```

List of stack
```
    > docker stack ls

    NAME                  SERVICES   ORCHESTRATOR
    my-swarm-stack-demo   6          Swarm

```

------
Multi compose stack deploy in swarm
```
    docker stack deploy --compose-file docker-compose.yml -c docker-compose.prod.yml <your-given-nane>
```
