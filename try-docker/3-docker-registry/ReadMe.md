# Container Registry


The Registry is a stateless, highly scalable server side application that stores and lets you distribute Docker images.


#### Why Container Registry?
If anyone wants to store there Images on private server not on Docker hub then
they can use this Registry services, and store/manages images over there. 
For this we need to define a **Port** to push our images on that **IP**.


#### How to create own Container Registry?

Step 1:
- server is ready to push image on IP:Port
```
    docker run --name trynow-registry -d -p 9090:5000 registry
```

Step 2:
```
    docker run -d -p 8000:80 --name my-nginx nginx

    > docker log my-nginx   # [check log]
```

Step 3:
```
    > docker image ls  [from here you can see the images]
    - syntax: docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]

    docker tag nginx 127.0.0.1:9090/private-nginx
```

Step 4:
- delete the original image
```
    docker image rm nginx:latest
```

Step 5:
- push you image to your private registry
```
    docker push 127.0.0.1:9090/private-nginx

    > docker push <IP>:<PORT>/<Image-Name>:v-1
```

Step 6:
- delete the original image
```
    docker image rm 127.0.0.1:9090/private-nginx:latest
```

Step 7:
- pull image from your private registry
```
    > docker pull <IP>:<PORT>/<Image-Name>:v-1

    > docker run -d -p 8000:80 --name my-nginx 127.0.0.1:9090/private-nginx
```
