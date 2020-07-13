FROM ubuntu:18.04

WORKDIR /app

COPY . /app

RUN apt-get update && \ 
    apt-get install --no-install-recommends -y python2.7 python2.7-dev python-pip python-setuptools && \
    rm -rvf /var/lib/apt/lists/*

RUN pip install --trusted-host pypi.python.org wheel && \
    pip install --trusted-host pypi.python.org -U pip && \
    pip install --trusted-host pypi.python.org -r requirements.txt

