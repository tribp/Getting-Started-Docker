# Docker-Getting-Started
Architecture: docker vs VM  
<img src="images/dockerVsVM.png" width="600px" >

## 1 Basic commands
### 1.1 docker version
```
docker --version
Docker version 18.03.0-ce, build 0520e24
```
```
docker version
Client:
 Version:	18.03.0-ce
 API version:	1.37
 Go version:	go1.9.4
 Git commit:	0520e24
 Built:	Wed Mar 21 23:06:22 2018
 OS/Arch:	darwin/amd64
 Experimental:	false
 Orchestrator:	swarm

Server:
 Engine:
  Version:	18.03.0-ce
  API version:	1.37 (minimum version 1.12)
  Go version:	go1.9.4
  Git commit:	0520e24
  Built:	Wed Mar 21 23:14:32 2018
  OS/Arch:	linux/amd64
  Experimental:	true
```
### 1.2 docker info
```
docker info
```
### 1.3 List docker images
```
docker images ls

```
### 1.4 List docker running containers  
remark: container = runtime instance of image
```
docker ps
docker container ls                         -> shows running container
docker container ls --all                   -> shows running + stopped containers
docker container ls -aq (all quiet mode)
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                                      NAMES
cf82029d460a        cs50/ide            "node server.js -w /…"   2 weeks ago         Up 5 days           0.0.0.0:5050->5050/tcp, 0.0.0.0:8080-8082->8080-8082/tcp   ide50
```
### 1.5 Execute docker image (or test)
```
docker run hello-world
docker container run -d -p 8080:80 --name myWebServer nginx     
    -> -d = in'detatch' mode (as process)
    -> map external port 8080 to internal port 80 inside container
    -> --name = give name
    -> nginx = name of image to use

```
### 1.6 Analyze containers
```
docker container top myWebServer        -> shows processes inside my container
docker container inspect myWebServer    -> shows docker config file (json) for this container
docker container stats                  -> shows overall performance of all my containers
docker container stats myWenServer      -> shows performance details of my container

```
### 1.7 starting CLI inside of container

    2 options:

    a. docker container run -it ... -> start a container interactively in the same process.
        if we leave CLI then container stops !!!
    b. docker container exec -it .. -> starts a cli on running container in ADDITIONAL process.
        if we leace CLI then CLI stops but container continues !!!
```
docket container exec -it myWebServer sh
    -> exec = execute command
    -> -i = interactive (stay open)
    -> -t = tty
    -> sh = shell command in nginx because there is no 'bash'
    
```
### 1.8 (Default) launch command

<img src="images/docker_Container_default_Cmd.png" width="800px" >

### 1.9 Different Linux Distros.

Most minimal = 'alpine' -> we have to install everything we need  additionally wit APK packege manager

docker container run it --name mySmallLinux alpine sh
docker container run it --name myUbuntu ubuntu bash

<img src="images/Linux_alpine_vs_ubuntu.png" width="800px" >

Next we have to add the things we need in alpine: eg 'curl'
```
docker pull alpine                                          -> pulls latest image of alpine
docker container run -it --name mySmallLinux alpine sh      -> start container + shell
(now in alpine prompt)
apk add curl                                                -> add curl to the (tiny) linux distro                                        
```
### 1.10 stopping and deleting

First we have to 'stop' a container before we can delete them
<img src="images/Docker_Container_Stop.png" width="800px" >

```
docker container stop ec8                   -> if eg ID=ec8532baxx etc (only first digits if unique)
or
docker container stop mySmallLinux
docker container rm mySmallLinux
```

#### Remark:

We can launch execute and delete (--rm) a container. This way nothing remains to be cleand-up.!!!

eg: Here we launch a linux 'centos' container, connect in into network my_DockerNet, and execute a curl command. This example queries a elasticsearch instance on port 9200.

```
docker container run --rm --network my_DockerNet centos curl -s esServerFarm:9200
```
### 1.11 Docker Networks

```
docker network ls
docker network inspect                                  -> returns json with network info and connected containers
docker network --create driver
docker network connect [options] NETWORK CONTAINER      -> connect CONTAINER to this NETWORK
docker network disconnect
```


Ping between containers

We perform a usual 'docker container exec -it' (to start new process where next cmd will be run) + container Name + command.
### Remark: 
DNS is default enabled with all custom networks but NOT at default 'bridge' network.
Best practise = create allways your own network(s)
```
docker container exec -it mySmallLinux ping myWebServer
```
<img src="images/Docker_ping_internalContainers.png" width="800px" >

#### 1.11.1 Docker DNS - network alias - round robin

We create 2 different servers (containres) but with the same '--network-alias'. This way DNS will resolve, round robin wise' each server ip address and creates some kind oh high availability.

'''
docker container run -d --name esServer1 elasticsearch:5.6 --network my_DockerNet --network-alias esCloudServer
'''

#### 1.11.2 Excercise:
- Make two elasticsearch containers (version 2) in network 'my_DockerNet' and both with network-alias = 'esServerFarm'
- launch a linux 'alpine' container and execute 'nslookup esServerFarm' to check resolving both ip's and -rrm (to clean-up)
- launch a 'centos' linux (also with --rm) and execute 'curl -s esServerFarm:9200' to check elasticsearch functionality.

```
docker container run -itd --name esServer1 --network my_DockerNet --network-alias esServerFarm elasticsearch:2
docker container run -itd --name esServer1 --network my_DockerNet --network-alias esServerFarm elasticsearch:2
docker container run --rm -it --network my_DockerNet alpine nslookup esServerFarm
docker container run --rm -it --network my_DockerNet centos curl -s esServerFarm:9200
```
<img src="images/Docker_Alpine_cmd_nslookup.png" width="800px" >

<img src="images/Docker_centos_cmd_elastic.png" width="800px" >

## 2 Images

### 2.1 Image basics
'''
What is an image ?
    - app binaries and dependencies
    - metadate about the image and how to run it
'''
### 2.2 Image layers
 
 ```
docker history nginx                    -> shows the layered changes in time of the image
docker image inspact nginx              -> shows json metadata
```
    - every layers has his unique SHA
    - every layer exits only ONCE, even if multiple image use that same layer
        eg: an image of a ubuntu + apt + apache AND an other image ubuntu + apt + mysql. While downloading the second image will only download mysql since ubuntu + apt is already present in an other image. The SHA ensures that we refer to exactly the correct and unique immage. 
### 2.3 Conclusion
    - images are made up of file system changes and metadata
    - each layer is uniquely identified and only stored ONCE on a host
    - this saves stores space on host and transfer time push/pull
    - a container is just a single read/write layer on top of image.
    
## 3 Docker hub
### 3.1 intro
    - 'official' images like 'nginx'
    - 'unofficial' = username / image_name  -> eg tribp/nginx
### 3.2 tags
    - add it manually or default = 'latest'
    - docker image tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]
        eg: docker image tag nginx tribp/nginx:testing
### 3.3 Login-out to docker hub
    - remark:
        - cat .docker.config.json       -> login key is added !! -> be sure to log out on untrusted host
    - docker login
    - docker logout
### 3.4 push / pull

Docker hub works similar to GitHub.
'''
    - docker image push tribp/nginx
'''

### remark: 
if we want private images, we first have to create a private respository on the docker hub account and push your image.
    
