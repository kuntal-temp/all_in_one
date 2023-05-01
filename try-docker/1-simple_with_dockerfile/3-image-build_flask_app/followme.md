## simple webapp with docker


**To build your image using the Dockerfile**
```
    - docker build .   [this cmd will return a random Build ID]
    - docker build -t username/project-name:version-name .  [tagging during creation of image]
```

**To Run the Image within Container**
```
    - docker run <build-id>
    - docker run username/project-name:version-name
```


By default flask app will run on port 5000 within container but this is not accessible untill we do port mapping

**How to map container port with system port?**
```
    syntax: docker run -p <system_port>:<container_port> <tag-name>

    - docker run -p 5000:5000 <tag-name>
    - docker run <build-id> [docker will give you one ip and port to access your app]
```