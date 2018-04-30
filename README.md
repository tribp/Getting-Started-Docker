# Docker-Getting-Started
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
Docker info
```
3. List docker images
```
docker images ls

```
4. List docker running containers   
remark: container = runtime instance of image
```
docker ps
'''
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                                      NAMES
cf82029d460a        cs50/ide            "node server.js -w /…"   2 weeks ago         Up 5 days           0.0.0.0:5050->5050/tcp, 0.0.0.0:8080-8082->8080-8082/tcp   ide50
```

