## Install Kubernetes on Linux


**Install Minikube**
Step 1:
```
    curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
```
Step 2:
```
    sudo install minikube-linux-amd64 /usr/local/bin/minikube
```
Step 3:
```
    sudo usermod -aG docker $USER && newgrp docker [Not needed if already done during docker install]
```
Step 4:
```
    - minikube start  [it will take some time]
    - minikube status [check status after that]
```

**Install kubectl**
Step 1:
```
    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
```
Step 2:
```
    sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```
Step 3:
```
    kubectl version
```


## My kubectl version
Client Version: version.Info{Major:"1", Minor:"22", GitVersion:"v1.22.4", GitCommit:"b695d79d4f967c403a96986f1750a35eb75e75f1", GitTreeState:"clean", BuildDate:"2021-11-17T15:48:33Z", GoVersion:"go1.16.10", Compiler:"gc", Platform:"linux/amd64"}

Server Version: version.Info{Major:"1", Minor:"22", GitVersion:"v1.22.3", GitCommit:"c92036820499fedefec0f847e2054d824aea6cd1", GitTreeState:"clean", BuildDate:"2021-10-27T18:35:25Z", GoVersion:"go1.16.9", Compiler:"gc", Platform:"linux/amd64"}


# More om kubectl
```
> minikube dashboard  or  minikube dashboard --url
> minikube start
> minikube stop
> minikube status
> minikube delete
```


----------------------
----------------------


## What is kubectl?
kubectl. The Kubernetes command-line tool, kubectl, allows you to run commands against Kubernetes clusters. You can use kubectl to deploy applications, inspect and manage cluster resources, and view logs.

## What is minikube?
minikube is a tool that lets you run Kubernetes locally. minikube runs a single-node Kubernetes cluster on your personal computer


## Note
If you want run & deploy your app on k8s then First make sure that, **minikube** is running.

If you are facing, this below error then 
```
    unable to connect to the server: dial tcp 192.168.49.2:8443: connect: no route to host
``` 

Run this below command
```
    > minikube start
```
