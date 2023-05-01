# Single Node Swarm

To check swarm is active or not?
```
    > docker info  [see the output]

    ...... so on
    Swarm: inactive
    ...... so on
```

To active Swarm
```
    > docker swarm init

    Output:

    Swarm initialized: current node (c7tydclmn9w5n0n2ns9ax51hd) is now a manager.
    To add a worker to this swarm, run the following command:
        docker swarm join --token SWMTKN-1-28wpo17welv3t4i4luked2qu3cfuh74h7xdxthcqyryr8eq4-4tpi52elv3knyeroyuwj25fla 192.168.130.128:2377
    To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.
```

List of Node
```
    > docker node ls
```


To check all services
```
    > docker service ls

    Output:
    ID             NAME            MODE         REPLICAS   IMAGE           PORTS
    9vmas55voj0t   busy_dubinsky   replicated   1/1        alpine:latest 
```

To get the all running Container details
```
    > docker ps
```

To get the Container details for a particular services
```
    - stntax: docker service ps <service-id/sercice-name>
    
    > docker service ps busy_dubinsky

    Output:
    ID             NAME              IMAGE           NODE      DESIRED STATE   CURRENT STATE           ERROR     PORTS
    y951863fgfk5   busy_dubinsky.1   alpine:latest   ubuntu    Running         Running 5 minutes ago
```

To create a new services
```
    Example 1:

    > docker service create alpine ping 8.8.8.8

    Output:
    9vmas55voj0tjxqsv8f4mqoz7
    overall progress: 1 out of 1 tasks 
    1/1: running   [==================================================>] 
    verify: Service converged
```

**Note:**
[docker service update] command used for to update the config without stopping container
For more: docker update --help
For more: docker service update --help



Now if we want to upsale our running services
```
    [creating 4 replicas]

    > docker service update 9vmas55voj0t --replicas 4

    Output:
    9vmas55voj0t
    overall progress: 4 out of 4 tasks 
    1/4: running   [==================================================>] 
    2/4: running   [==================================================>] 
    3/4: running   [==================================================>] 
    4/4: running   [==================================================>] 
    verify: Service converged
```

To check all the container that are create
```
    > docker container ls or docker ps

    Output:
    CONTAINER ID   IMAGE           COMMAND          CREATED          STATUS          PORTS     NAMES
    b187afdee8b0   alpine:latest   "ping 8.8.8.8"   3 minutes ago    Up 3 minutes              busy_dubinsky.3.lw2b3gzov3tfmme3f8vs1isa4
    9dd428d2ce83   alpine:latest   "ping 8.8.8.8"   3 minutes ago    Up 3 minutes              busy_dubinsky.4.wj727rmj5itpsoybl31bb9yel
    9a3f285477f4   alpine:latest   "ping 8.8.8.8"   3 minutes ago    Up 3 minutes              busy_dubinsky.2.s5jsnptusjyisf6yopy3w3zsj
    337ee0653da5   alpine:latest   "ping 8.8.8.8"   17 minutes ago   Up 17 minutes             busy_dubinsky.1.y951863fgfk57qyx7328roq44
```

Now if at point one container goes down or If I rm it then it will create a new container
automatically to maintain the replicas config we did [all time 4 container running]

Let's remove one container and check again list of all containers
```
    > docker rm -f b187afdee8b0

    > docker ps     [see create time]
```

To remove a services
```
   - syntax: docker service rm <srvices-name/services-id>

    > docker service rm busy_dubinsky   [it will remove all the container created by this service as well]
```
