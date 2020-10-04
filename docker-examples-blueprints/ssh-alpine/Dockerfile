FROM python:3.7.3-alpine3.9

RUN mkdir /work/
WORKDIR /work/


COPY . /work/

##enable SSH for development
RUN echo 'root:root' | chpasswd
RUN apk upgrade
RUN apk update
RUN apk add --no-cache openssh 
RUN ssh-keygen -A \
    && sed -i 's/#*PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
    && sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config \
    && sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication no/' /etc/ssh/sshd_config \
    && sed -i 's/#Port 22/Port 5022/g' /etc/ssh/sshd_config


CMD ["/usr/sbin/sshd","-D"]