FROM ubuntu:16.04

RUN apt-get update -qq && \
    apt-get install -qq -y -o quiet=1 \
    build-essential libexpat1-dev zlib1g-dev libbz2-dev wget \
    python python-pip python-setuptools python-dev libboost-python-dev


WORKDIR /app
ADD . /app

COPY deps ./
RUN pip install -r deps/requirements.txt

COPY osm-fudge ./
CMD ./worker.sh