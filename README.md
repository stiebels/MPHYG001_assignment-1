# Greengraph Package

Greengraph is a software package written in Python that was created and packaged as part of theassessment for the course MPHYG001 at University College London:
http://github-pages.ucl.ac.uk/rsd-engineeringcourse/


The package enables the user to generate a graph of the proportion of green pixels in a series of satellite images between two geographical points.

The Greengraph package includes two main classes that incorporate the functionality:

1. <b><code>Map</code></b> - This class takes latitude and longitude as input parameters, then obtains a map using the GoogleMaps API as PNG and eventually computes the number of green pixels on the PNG image.
2. <b><code>Graph</code></b> - This class takes two locations as input parameters, obtains its latitude and longitude parameters using the GoogleMaps API, then calls the class Map to return the number of green pixels between the two locations.


<b>Description of the command line interface:</b>

```
usage: greengraph [-h] [-s STEPS] begin end

Generates a graph that displays the number of green
pixels per step between two geographical locations.

positional arguments:
  begin       Enter start location, e.g. 'London' .
  end         Enter location of target destination,
              e.g. 'Cambridge'.

optional arguments:
  -h, --help  show this help message and exit
  -s STEPS    Steps between begin and end, e.g. '10'.
```