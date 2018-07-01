#!/usr/bin/env bash

wget ${PBF_URL} -O data.pbf
python3 osm_fudge/osm/amenities.py --input data.pbf
