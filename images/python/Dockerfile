FROM python:latest

ARG VCS

RUN apt-get update
RUN apt-get install -y \
            $VCS \
            default-mysql-server \
            default-mysql-client
RUN apt-get clean

ARG USERNAME
ARG PASSWORD

RUN useradd -s /bin/bash -md /home/$USERNAME -p $(openssl passwd -1 $PASSWORD) $USERNAME

ARG REPOSITORY
RUN $VCS clone $REPOSITORY /home/$USERNAME/repository

WORKDIR /home/$USERNAME/repository

RUN pip3 install -r requirements.txt

COPY config.tmp.py .

RUN mkdir /srv/docker
COPY entrypoint.sh /srv/docker

ENV USER=$USERNAME

ENV MYSQL_USERNAME=$USERNAME
ENV MYSQL_PASSWORD=$PASSWORD

CMD "/srv/docker/entrypoint.sh"