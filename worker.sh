#!/usr/bin/env bash

wget ${PBF_URL} -O data.pbf
python osm-fudge/amenity-example.py data.pbf