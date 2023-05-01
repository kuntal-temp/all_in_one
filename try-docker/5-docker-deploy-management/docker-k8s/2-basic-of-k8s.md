# Basic Of K8S


# Create deployments
```
    > kubectl create deployment my-nginx --image=nginx:1.16.1  [deployment.apps/my-nginx created]
```

# Port Expose
```
    > kubectl expose deployment web --type=NodePort --port=8080

    kubectl expose deployment my-nginx --port 8000
    kubectl expose deployment my-nginx --port=8081 --target-port=3000 -name=service-name
```

# Expose to World
```
    > minikube service web --url
```


# List of deployments
```
    > kubectl get deployments
    > kubectl get deploy
```

# Get details of your Deployment
```
    > kubectl describe deployments
```

# Update your Deployment:
```
    > kubectl set image deployment nginx-deployment nginx=nginx:1.16.1
```

# Edit deployment
```
    > kubectl edit deployment nginx-deployment
```

# Deployment rollout status
```
    > kubectl rollout status deployment nginx-deployment
```


# To see the pod list
```
    > kubectl get pods
    > kubectl get pods --show-labels
    > kubectl get pods -A
```

# To see the replica set list
```
    kubectl get rs
```

# To see all the services
```
    kubectl get services
```

# To see all the objects
```
    kubectl get all
```

# Clean Up
```
    > kubectl delete service my-nginx
    > kubectl delete deployment my-nginx
```

# How to remove pods & deployment
```
    > kubectl delete pod my-nginx  [delete pods]
    > kubectl delete deployment my-nginx  [delete deployment]
    > kubectl delete services my-nginx  [service "my-nginx" deleted] [if expose used]
```


---------------

To get the log of any deployment objects
```
    kubectl logs deployment my-nginx
```

To get the details of a pod
```
    - syntas: kubectl describe <pod-name>

    > kubectl describe pod/my-apache-7b68fdd849-5lns4
```

To delete a particular pod
``` 
    - syntas: kubectl delete <pod-name>

    > kubectl delete pod/my-apache-7b68fdd849-5lns4
```

https://www.howtogeek.com/devops/kubernetes-clusterip-nodeport-or-ingress-when-to-use-each/

