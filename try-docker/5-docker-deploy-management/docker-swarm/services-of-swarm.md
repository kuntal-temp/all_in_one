# Create service for Docker Swarm


- Services can only be created on a manager.

Example:
```
docker service create \
  --name my-nginx \
  --publish target=80, published=80 \
  --replicas=5 \
  --network nginx-net \
  nginx
```


List of all services
```
    docker service ls
```


Create service
```
  docker service create --name redis redis:3.0.6

  or

  docker service create --name redis --replicas=5 redis:3.0.6

  or

  docker service create --name my_web --replicas 3 --publish 8080:80 nginx
```


Get Details Information for a services
```
    docker service inspect my-nginx
```


#### More service command
```
  > docker service logs <service-name>

  > docker service inspect <service-name>

  > docker service update -p 9000:8000 <service-name> 
  or 
  docker service update --replicas=5 <service-name>
```
