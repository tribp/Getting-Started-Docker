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
docker container ls
docker container ls --all
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
6. starting CLI inside of container
```
docket container exec -it myWebServer sh
    -> exec = execute command
    -> -i = interactive (stay open)
    -> -t = tty
    -> sh = shell command in nginx because there is no 'bash'
    
```
7. Analyze containers
````
docker container top myWebServer        -> shows process inside my container
docker container inspect myWebServer    -> shows docker config file (json) for this container
docker container stats                  -> shows overall performance of all my containers
docker container stats myWenServer      -> shows performance details of my container

```

