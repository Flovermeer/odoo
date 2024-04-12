FROM ubuntu:22.04

# install python 3.10
RUN apt update && \ 
    apt install -y python3.10 && \
    apt install -y python3-pip


