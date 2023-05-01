# It is reaquied for Container to Control traffic inside a single Swarm


**Note:**
Each service can connect to Different Network

- creates an overlay network named ingress for publishing service ports external to the swarm.


How to create Overlay Network?
```
    - syntax: docker network create --driver overlay <your-network-name> 

    docker network create --driver overlay my-demo-network


    -> [This will be created]
    1xflxt2x81qe   ingress           overlay   swarm   # [swarm default one]
    v1bldba4vnch   my-demo-network   overlay   swarm 
```


How to Create Service using user define Newtowk?
```
    - syntax: docker service create --name <your-services-name> --network <your-network-name> <your-image-name>

    docker service create --name my-alp --network my-demo-network alpine ping 8.8.8.8
```


How to update network and remove old network for a service?
```
    docker service update --network-add <new-network> --network-rm <old-network> <service-name>
```


**Note:**
Now let's aasume your web-app is running as a different service and that app is using Postgres database which is running on as a another service. Now web-app can communicate with postgres server by using Host name.


Read More: https://docs.docker.com/network/network-tutorial-overlay/
