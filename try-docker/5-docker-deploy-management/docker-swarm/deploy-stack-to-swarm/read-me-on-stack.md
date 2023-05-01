# Deploy a stack to a swarm

Link: https://docs.docker.com/engine/swarm/stack-deploy/


**The build option is ignored when deploying a stack in swarm mode The docker stack command does not build images before deploying**


Step 1
```
    docker-compose up --build
```

Step 2
```
    docker-compose down
```


### Deploy the stack to the swarm

Step 1
```
    docker stack deploy --compose-file docker-compose.yml my-stack-demo
```

Step 2
```
    docker stack services my-stack-demo    # [all tasks list for this services]
```

To remove services from Stack
```
    docker stack rm my-stack-demo
```

To leave the swarm 
```
    [run this on node which user want to remove]

    docker swarm leave --force
```


-----------------------------------------------------------------------------
List Of all stack
```
    docker stack ls

    or

    docker stack ls --format "{{.Name}}: {{.Services}}"
```


List the tasks that are part of a stack
```
    docker stack ps <your-stack-name>
```

Remove a stack
```
    docker stack rm <your-stack-name>
```

Filtering on stack services
```
    ocker stack services --filter name=myapp_web --filter name=myapp_db <your-service-name>
```


-------
**Note:**

1) remove from stack
2) remove from serivce
3) remove from network
