FROM ubuntu:22.04

ENV TZ=Europe/Paris
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# install python 3.10
RUN apt update && \ 
    apt-get -y install sudo && \
    apt-get install -y python3.10 && \
    apt-get install -y python3-pip && \
    apt-get install -y python3-pypdf2 && \
    apt-get install -y libpq-dev && \
    apt-get install -y libsasl2-dev && \ 
    apt-get install -y python-dev-is-python3 && \ 
    apt-get install -y libldap2-dev && \
    apt-get install -y libssl-dev && \
    apt-get install -y postgresql #Debian/Ubuntu8 && \
    apt-get install -y inetutils-ping && \
    apt-get install -y wkhtmltopdf


RUN pip install psycopg2-binary
    
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
ENV PATH=/usr/pgsql-14/bin:$PATH