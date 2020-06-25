FROM ubuntu:16.04

WORKDIR /app

COPY . /app

RUN apt-get update

RUN apt-get install -y build-essential python3.5 python3.5-dev python3-pip

RUN pip3 install --trusted-host pypi.python.org wheel

RUN pip3 install --trusted-host pypi.python.org -U pip

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt
