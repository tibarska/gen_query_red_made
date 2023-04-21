FROM ubuntu:trusty
# COPY apt.conf /etc/apt/apt.conf
RUN sudo apt-get -y update
RUN sudo apt-get -y upgrade
RUN sudo apt-get install -y sqlite3 libsqlite3-dev
RUN mkdir -p /volume/db
RUN mkdir data

COPY db_init.sh /db_init.sh
COPY init.sql /init.sql

CMD /bin/bash
