# docker secret


- Way-1 [not safe]
```
    printf "my super secret password" | docker secret create my_secret -
```

- Way-2 [file based]
```
    docker secret create my_secret ./secret.json
```

- List of 
```
    docker secret ls
```

- Create a secret with labels
```
    docker secret create --label env=dev --label rev=20170324 my_secret ./secret.json
```

Remove secret
```
    docker secret rm secret.json
```


**Note:** we can create config same way as we created secret
 