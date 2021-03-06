FROM ubuntu:16.04

RUN apt-get update -qq && \
    apt-get install -qq -y -o quiet=1 \
    build-essential libexpat1-dev zlib1g-dev libbz2-dev wget \
    python3 python3-pip python3-setuptools python3-dev libboost-python-dev


COPY deps /deps
RUN pip3 install -r deps/requirements.txt

WORKDIR /app
ADD . /app

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

COPY osm_fudge ./
CMD ./worker.sh
