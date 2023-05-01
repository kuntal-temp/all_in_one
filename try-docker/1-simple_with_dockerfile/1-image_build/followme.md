## command for first image build and run container 


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
