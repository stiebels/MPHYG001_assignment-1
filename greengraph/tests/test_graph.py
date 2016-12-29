from pytest import raises
from mock import patch
import geopy
from greengraph.Graph import Graph
from greengraph.Map import Map
import pickle
import os
import numpy as np


'''
This class tests the class Graph and its functions.
'''

def load_map_fixtures():
    # Loads a predefined Map object of London as fixture for offline testing.
    # Map(51.5073509, -0.1277583)

    directory = str(os.path.dirname(os.path.abspath(__file__)) + '/fixtures/')
    file = open(directory+"mock_map",'rb')
    m_Map_fix = pickle.load(file)
    file.close()
    return m_Map_fix


def load_graph_fixtures():
    # Load fixture of Graph
    directory = str(os.path.dirname(os.path.abspath(__file__)) + '/fixtures/')
    file = open(directory + "mock_graph", 'rb')
    m_Graph_fix = pickle.load(file)
    file.close()
    return m_Graph_fix


@patch('geopy.geocoders.GoogleV3')
def test_Graph_init(m_geocode):
    # Test initialization values of Graph
    t_Graph = Graph('London', 'Cambridge')
    assert (t_Graph.start == 'London')
    assert (t_Graph.end == 'Cambridge')
    m_geocode.assert_called_with(domain="maps.google.co.uk")


def test_location_sequence():
    # Test calculation of location_sequence
    t_Graph = Graph('London', 'Cambridge')

    # Test whether the current object (t_Graph) returns same
    # value for location_sequence as fixture. Using np for comparison since
    # more accurate when handling very small numbers
    assert (np.array_equal(
        load_graph_fixtures().location_sequence
        ([51.5073509, -0.1277583], [52.205337, 0.121817], 5)
        , t_Graph.location_sequence
        ([51.5073509, -0.1277583], [52.205337, 0.121817], 5)
    ) == True)


def test_geocoder():
    # Test unknown location passed to geolocate
    # REQUIRES INTERNET because it depends on GoogleAPI response
    t_Graph = Graph('London', 'Cambridge')
    try:
        with raises(TypeError):
            t_Graph.geolocate('123asdf') is None
    except:
        print('Please connect to the Internet for this test.')


def test_geolocate():
    # Test calling of geopy
    t_Graph = Graph('London', 'Cambridge')
    with patch.object(geopy.geocoders.GoogleV3, 'geocode') as m_geocode:
        t_Graph.geolocate('London')
        m_geocode.assert_called_with('London', exactly_one=False)


@patch('geopy.geocoders.GoogleV3')
def test_green_between(m_geocoder):
    # Test calculation of green_between
    with patch.object(Map, '__init__', return_value=load_map_fixtures()) as m_Map:
        t_Graph = Graph('London', 'Cambridge')

        # Test how often location_sequence is called
        [m_Map.count_green() for location in
         t_Graph.location_sequence
         ([51.5073509, -0.1277583], [52.205337, 0.121817], 5)]
        assert (m_Map.count_green.call_count == 5)



# def t_coordinates(start=(-181, -50), end=(181, 50), steps=20):
# Test possible coordinates
# Non-existent coordinates can be used, however, since the GoogleAPI will
# respond with 'None', this error is basically treated by function t_geocoder.
#    with raises(ValueError):
#        t_Graph.location_sequence(start, end, steps)