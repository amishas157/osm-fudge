FROM ubuntu:16.04

RUN apt-get update -qq && \
    apt-get install -qq -y -o quiet=1 \
    build-essential libexpat1-dev zlib1g-dev libbz2-dev \
    python python-pip python-setuptools python-dev libboost-python-dev

WORKDIR /app
ADD . /app

COPY deps ./
RUN pip install -r deps/requirements.txt

COPY data ./
COPY osm-fudge ./

CMD python osm-fudge/amenity-example.py data/monaco-latest.osm.pbf