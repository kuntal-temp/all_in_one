## Learn Docker in Kuntal Style


- How to install Docker on Linux?
```
  > sudo apt-get update
  > sudo apt install apt-transport-https ca-certificates curl software-properties-common
  > curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
  > sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
  > sudo apt install docker-ce
```

- How to check docker status?
```
  > sudo systemctl status docker
```

- Executing the Docker Command Without Sudo
```
    > sudo usermod -aG docker ${USER}
    > su - ${USER}
```

- How to add a user to the docker group that you’re not logged in as, declare that username explicitly
```
    > sudo usermod -aG docker <username>
```


--------------------------------------------------------------------------------------

- How to install docker-compose on Linux?
```
  > sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

  > sudo chmod +x /usr/local/bin/docker-compose
```

- Check docker-compose Installation
```
  > docker-compose --version
```

- Uninstall docker-compose
```
  > sudo rm /usr/local/bin/docker-compose
```

------
Learn docker official: https://docs.docker.com/get-started/overview/

docker-compose install: https://docs.docker.com/compose/install/

Guide on Dockerfile: https://docs.docker.com/engine/reference/builder/

Guide on docker-compose.yml: https://docs.docker.com/compose/compose-file/compose-file-v3/
