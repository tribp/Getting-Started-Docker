# Alpine container with SSH

## 1. Intro and why ?

Normally we don't need ssh in a container because:
- typically a container runs 1 process = his task it had to perform
- we  can use  "docker exec -it my_container_name /bin/sh"

## 2. VScode remote development with ssh

In VScode we can use the extension "Remote-SSH", login via VScode into a remote container and debug code running inside this container.

Problem:

VScode has to install code inside the container to connect the remote IDE but , for the time beiing, does not support "alpine" linux because alpine is **musl** based instead of **glibc**

Conclusion:

This blueprint will work. You can ssh into the container but not it wil not work with VScode. VScode will be able to login but stop because of the lack of "alpine"(msul) support. 

If you need a small linux container to works with VScode-Remote-SSH, you can opt for another linux image like "Debian-buster-slim" (see other blueprint)

## 3. SSH port 22

SSH standard port is 22. A typical scenario is where you have a remote machine, hosting your containers who share the same public ip. Typically you will use port 22 to ssh into the hast and thus you need to assign other ports for SSH into the containers. 

We can use different strategies:

- config the ssh server to use other port than 22. This can be achieved by changing ths default port in /etc/ssh/sshd_config. But bugs were reported so it is not adviced, and not needed, since we can use the solution below. 
- port mapping on the container:
    - "docker run -d -p 5022:22 my_image"
    or
    - config in docker-compose

## 4. Configuration:

```
#build your image
docker build -t my_image . 

# Or manually run container
docker run -d --rm -p 5022:22 my_image 

# Or automated with docker-compose
docker-compose up -d

# ssh into container from your computer
ssh  -p 5022 root@192.168.2.152

```

