import numpy as np
import geopy
from greengraph.Map import Map


'''
This class takes latitude and longitude as input parameters,
then obtains a map as PNG using the GoogleMaps API
and eventually computes the number of green pixels on the PNG image.
'''


class Graph(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.geocoder = geopy.geocoders.GoogleV3(domain="maps.google.co.uk")

    def geolocate(self, place):
        return self.geocoder.geocode(place, exactly_one=False)[0][1]

    def location_sequence(self, start, end, steps):
        lats = np.linspace(start[0], end[0], steps)
        longs = np.linspace(start[1], end[1], steps)
        return np.vstack([lats, longs]).transpose()

    def green_between(self, steps):
        return [Map(*location).count_green()
                for location in self.location_sequence(
                self.geolocate(self.start),
                self.geolocate(self.end),
                steps)]