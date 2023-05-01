# Basic Of Swarm

Link: https://docs.docker.com/engine/swarm/swarm-mode/


When you first install and start working with Docker Engine, swarm mode is disabled by default

- by default, generates a self-signed root CA for the swarm
- by default, generates tokens for worker and manager nodes to join the swarm
- creates a swarm named default
- names the node with the machine hostname
- creates an overlay network named ingress for publishing service ports external to the swarm
- creates an overlay default IP addresses and subnet mask for your networks



Basically 3 types of Node are present in Swarm
- Leader
- Manager
- worker


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


---
- **Note**

Swarm never creates individual containers.

Instead, all Swarm workloads are scheduled as services, which are scalable groups of containers with added networking features maintained automatically by Swarm.

YAML files describe all the components and configurations of your Swarm app, and can be used to easily create and destroy your app in any Swarm environment
