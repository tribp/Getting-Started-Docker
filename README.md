# Docker-Getting-Started
Architecture: docker vs VM  
<img src="images/dockerVsVM.png" width="600px" >

Basic commands
1. docker version
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
2. docker info
```
docker info
```
3. List docker images
```
docker images ls

```
4. List docker running containers  
remark: container = runtime instance of image
```
docker ps
docker container ls                         -> shows running container
docker container ls --all                   -> shows running + stopped containers
docker container ls -aq (all quiet mode)
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                                      NAMES
cf82029d460a        cs50/ide            "node server.js -w /…"   2 weeks ago         Up 5 days           0.0.0.0:5050->5050/tcp, 0.0.0.0:8080-8082->8080-8082/tcp   ide50
```
5. Execute docker image (or test)
```
docker run hello-world
docker container run -d -p 8080:80 --name myWebServer nginx     
    -> -d = in'detatch' mode (as process)
    -> map external port 8080 to internal port 80 inside container
    -> --name = give name
    -> nginx = name of image to use

```
6. Analyze containers
```
docker container top myWebServer        -> shows processes inside my container
docker container inspect myWebServer    -> shows docker config file (json) for this container
docker container stats                  -> shows overall performance of all my containers
docker container stats myWenServer      -> shows performance details of my container

```
7. starting CLI inside of container

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
8. (Default) launch command

<img src="images/docker_Container_default_Cmd.png" width="800px" >

9. Different Linux Distros.

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
10. stopping and deleting

First we have to 'stop' a container before we can delete them
<img src="images/Docker_Container_Stop.png" width="800px" >

```
docker container stop ec8                   -> if eg ID=ec8532baxx etc (only first digits if unique)
or
docker container stop mySmallLinux
docker container rm mySmallLinux
```
11. Docker Networks

```
docker network ls
docker network inspect
docker network --create driver
docker network connect
docker network disconnect
```