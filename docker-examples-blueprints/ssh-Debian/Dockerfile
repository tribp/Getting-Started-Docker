
FROM python:3.9-rc-slim-buster

RUN mkdir /work/
WORKDIR /work/


COPY . /work/

##enable SSH for development
RUN echo 'root:root' | chpasswd
RUN apt-get upgrade
RUN apt-get update
RUN apt-get -y install openssh-server supervisor wget
RUN sed -i 's/#*PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
    && sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config \
    && sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication no/' /etc/ssh/sshd_config
#    && sed -i 's/#Port 22/Port 5222/g' /etc/ssh/sshd_config

RUN mkdir /var/run/sshd; chmod 755 /var/run/sshd
RUN mkdir /root/.ssh; chown root. /root/.ssh; chmod 700 /root/.ssh
RUN ssh-keygen -A

ADD supervisord.conf /etc/supervisor/supervisord.conf
#ADD .ssh/id_rsa.pub /root/.ssh/authorized_keys

#CMD python -m debugpy --listen localhost:5678 --wait-for-client test.py
#CMD ["/bin/bash"]
CMD ["/usr/bin/supervisord"]

