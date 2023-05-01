# Docker Network


**Docker Network Basic CMD**
```
    - docker network ls

NETWORK ID     NAME      DRIVER    SCOPE
28582b110948   bridge    bridge    local
c5b99b9dcad4   host      host      local
```


### Bridge
The default network driver. If you don’t specify a driver, this is the type of network you are creating. Bridge networks are usually used when your applications run in standalone containers that need to communicate

Read More: https://docs.docker.com/network/network-tutorial-standalone/


### Overlay
Overlay networks connect multiple Docker daemons together and enable swarm services to communicate with each other.
You can also use overlay networks to facilitate communication between a swarm service and a standalone container, or between two standalone containers on different Docker daemons. This strategy removes the need to do OS-level routing between these containers.

Read More: https://docs.docker.com/network/network-tutorial-overlay/


```
    - docker network  [deatils and all container connected with this bridge and more.....]
```

**How to map container port with system port?**
let's assume your app is running on localhost:8000 than below cmd will to access your app
```
    syntax: docker run -p <system_port>:<container_port> <tag-name>

    - docker run -p 8000:80 nginx  [nginx is running on http://127.0.0.1:8000]

    - docker run -p 5000:5000 <tag-name>
    - docker run -p 5000:5000 <build-id>
    - docker run -p 8000:5000 <tag-name>

    - docker run <build-id> [docker will give you one ip and port to access your app]
```

**Create a Network**
```
    docker network create <my_network_name>  [by default driver will be bridge]

    How to use this network
    - docker run --network <my_network_name> ngnix

    docker network connect/disconnect [read it]
```
----------------------------------------------------------------------------

# Docker Network DNS

In docker container name is the hostname. 

Now let's assume two container running on same network, then both container
can communicate internally using DNS not ip. But if container running on diff network then ping will not work

Note:
All container are attached with Bridge Network and this is connected with Host using Nat protocol.
All the container which are attached with Bridge they can communicate internally.

Example:
**Step 1** [I created a network]
```
    docker network create my-network-100
```

**Step 2**
[2 nginx container are running in bg]
```
    - docker run --name nginx-10 --network my-network-100 -d nginx
    - docker run --name nginx-20 --network my-network-100 -d nginx

    [with port] docker run --name nginx-10 --network my-network-100 -p 8000:80 -d nginx
```

**Step 3**
```
    > docker port nginx-10   [show the port using for this container]

    80/tcp -> 0.0.0.0:8000
    80/tcp -> :::8000
```

**Step 4**
```
    > docker network inspect my-network-100   [show all container attachted to this network]
```

**Step 5**
```
    docker exec -it nginx-10 ping nginx-20  
    
    [if above cmd not work, ping not installed. Then run below then repeat above cmd]
    apt-get update
    apt-get install iputils-ping
```


# Docker network concept Testing
```
> docker network create my-network-100
> docker run --name bb1 --network my-network-100 -d busybox ping www.google.com
> docker run --name bb2 --network my-network-100 -d busybox ping www.google.com
> docker run --name aa1 -d busybox ping www.google.com

> docker network inspect my-network-100

> docker exec -it 102f75711ab1 sh => ifconfig => ping <container-2-ip> [same n/w]
> docker exec -it 102f75711ab2 sh => ifconfig => ping <container-1-ip> [same n/w]
> docker exec -it 102f75711ab3 sh => ifconfig => ping <container-1-ip> [deault n/w]

OR from:  bb1 ping bb2 [ping with dns]
```



-------------------------------------------------------------------------------------
### docker network ls
```
Output-> 
NETWORK ID     NAME             DRIVER    SCOPE
9850e41cfee9   bridge           bridge    local
c5b99b9dcad4   host             host      local
84baec395a55   my-network-100   bridge    local
0782687c4e69   none             null      local
```
