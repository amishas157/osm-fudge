#!/usr/bin/env bash

wget ${PBF_URL} -O data.pbf
python3 osm-fudge/amenity-example.py data.pbf