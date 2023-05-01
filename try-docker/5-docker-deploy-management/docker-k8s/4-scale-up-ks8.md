# Create Replica-Sets


## Example - 1
To test everything good or not?
```
    > kubectl run my-apache --image httpd  [pod created]

    > kubectl create deployment my-apache --image httpd  [deployment.apps/nginx created]
```

# Scale-up & Autoscale
```
    > kubectl scale deployment/my-apache --replicas 3

    > kubectl scale deployment/nginx-deployment --replicas=10

    > kubectl autoscale deployment/nginx-deployment --min=2 --max=15 --cpu-percent=80
```


To see the pod list
```
    kubectl get pods -w   # [same like watch cmd]
```

To see all the objects
```
    kubectl get all
```


How to remove pods & deployment
```
    > kubectl delete pod my-apache  [delete pods]
    
    > kubectl delete deployment my-apache  [delete deployment]
```
