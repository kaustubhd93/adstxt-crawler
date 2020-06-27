FROM ubuntu:16.04

WORKDIR /app

COPY . /app

RUN apt-get update

RUN apt-get install -y build-essential python2.7 python2.7-dev python-pip

RUN  pip install --trusted-host pypi.python.org wheel

RUN pip install --trusted-host pypi.python.org -U pip

RUN pip install --trusted-host pypi.python.org -r requirements.txt
