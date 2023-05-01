# Multi Node Swarm


**create 4 Node Swarm**
```
    https://labs.play-with-docker.com/  [use here]
```

### creating using  docker-machine in mac/windows locally

Basically 3 types of Node are present in Swarm
- Leader
- Manager
- worker

How to create node?
```
    [if only docker machine install or use cloud-instance as node]

    > docker-machine create node-1
    > docker-machine create node-2
    > docker-machine create node-3
    > docker-machine create node-4
```

List of Node
```
    > docker node ls
```

How to connect with newly created node?
```
    > docker-machine ssh node-1
```

To active Swarm on any of the node then rest of the nodes will be connected with this node, using join cmd [Assume I run it in Node-1]
```
    In Node-1 run: [this is now manager]
    > docker swarm init

    Output:

    Swarm initialized: current node (c7tydclmn9w5n0n2ns9ax51hd) is now a manager.
    To add a worker to this swarm, run the following command:
        docker swarm join --token SWMTKN-1-28wpo17welv3t4i4luked2qu3cfuh74h7xdxthcqyryr8eq4-4tpi52elv3knyeroyuwj25fla 192.168.130.128:2377
    To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.
```

Then ssh to 2nd node and join that node to node-1 [do this for all node]
```
    In Node-2 run:  [added as worker]
    > docker swarm join --token SWMTKN-1-28wpo17welv3t4i4luked2qu3cfuh74h7xdxthcqyryr8eq4-4tpi52elv3knyeroyuwj25fla 192.168.130.128:2377

    Now Node-2 is added swarm as a worker
```


**Note:**
Node-1 is now Leader and Node-2 is the workers node


How to add Node-3 as a Manager?
```
    In Node-1 run:
    > docker swarm join-token manager

    Output:
    To add manager ..........
        docker swarm join --token SWMTKN-1-28wpo17welv3t4i4luked2u3cfuh74h7xdxthcqyryr8eq4-4tpi52elv3knyeroyuwj25fla 192.168.130.128:2378
    ......... so on


    In Node-3 run:
    > docker swarm join --token SWMTKN-1-28wpo17welv3t4i4luked2u3cfuh74h7xdxthcqyryr8eq4-4tpi52elv3knyeroyuwj25fla 192.168.130.128:2378

    Now Node-3 is added swarm as a manager
```

How to make a worker node to Manager node?
```
    docker node update --role manager Node-2
```

How to leave a worker node from Swarm?
```
    [Go to that particular node]

    > docker swarm leave
```
