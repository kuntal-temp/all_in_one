## travis-ci


**Diagram View**
------------------------------------------------------------------
![travis-ci](https://user-images.githubusercontent.com/39960418/143720694-a8951a13-e423-4fa5-9501-527554fbadc3.png)


**language: generic**
You can set language: minimal or language: generic which are not language specific.

- language: minimal
```
version control tools
essential build tools such as gcc and make
network tools such as curl and essential
Docker
python
```

- language: generic
```
generic extends minimal and additionally includes:
databases and services
go
jvm
node_js
php
ruby
```
