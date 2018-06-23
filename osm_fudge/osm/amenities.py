#!/usr/bin/env python3

"""
Extract all objects with an amenity tag from an osm file and list them
with their name and position.
"""
import osmium as o
import argparse


class AmenityListHandler(o.SimpleHandler):

    def print_amenity(amenity, tags, lon, lat):
        name = tags.get('name', '')
        print("{name}".format(name=name))

    def node(self, n):
        if 'amenity' in n.tags and 'name' in n.tags:
            self.print_amenity(n.tags, n.location.lon, n.location.lat)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Collects data from osm pbf file')
    parser.add_argument('--input', type=str, required=True, help='File for creating input data')
    args = parser.parse_args()

    handler = AmenityListHandler()
    handler.apply_file(args.input)
