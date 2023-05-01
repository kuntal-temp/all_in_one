# Basic Of K8S


# Create deployments
```
    > kubectl create deployment my-nginx --image=nginx:1.16.1  [deployment.apps/my-nginx created]
```

# List of Pods
```
    > kubectl get pods
```

# port-forward
```
    > kubectl port-forward nginx-554b9c67f9-rwbp7 8080:80
```

Access it from: http://127.0.0.1:8080/



https://rtfm.co.ua/en/kubernetes-clusterip-vs-nodeport-vs-loadbalancer-services-and-ingress-an-overview-with-examples/

