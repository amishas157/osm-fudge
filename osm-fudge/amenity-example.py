#!/usr/bin/env python3

"""
Extract all objects with an amenity tag from an osm file and list them
with their name and position.
"""
import osmium as o
import sys

class AmenityListHandler(o.SimpleHandler):

    def print_amenity(amenity, tags, lon, lat):
        name = tags.get('name', '')
        print("{lon}, {lat}, {tags[amenity]}, {name}")

    def node(self, n):
        if 'amenity' in n.tags and 'name' in n.tags:
            self.print_amenity(n.tags, n.location.lon, n.location.lat)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python amenity-example.py <osmfile>")
        sys.exit(-1)

    handler = AmenityListHandler()

    handler.apply_file(sys.argv[1])