from pytest import raises
from mock import Mock, patch, MagicMock
import numpy as np
import geopy
from greengraph.Graph import Graph
from greengraph.Map import Map


t_Graph = Graph('London', 'Cambridge')


@patch('geopy.geocoders.GoogleV3')
def t_Graph_init(m_geocode):
    # Test initialization values of Graph
    t_Graph = Graph('London', 'Cambridge')
    assert (t_Graph.start == 'London')
    assert (t_Graph.end == 'Cambridge')
    m_geocode.assert_called_with(domain="maps.google.co.uk")


def t_location_sequence():
    # Test calculation of location_sequence
    to_be = np.array([[-10., -10.], [-5., -5.], [0., 0.], [5., 5.], [10., 10.]])
    assert (t_Graph.location_sequence((-10, -10), (10, 10), 5) == to_be).all


def t_geocoder():
    # Test unknown location passed to geolocate
    with raises(TypeError):
        t_Graph.geolocate('123asdf') is None


def t_geolocate():
    # Test calling of geopy
    with patch.object(geopy.geocoders.GoogleV3, 'geocode') as m_geocode:
        t_Graph.geolocate('London')
        m_geocode.assert_called_with('London', exactly_one=False)


def t_green_between():
    # Test calculation of green_between
    m_sequence = [0, 0, 0, 0, 93575]
    with patch.object(Map, '__init__') as m_Map:
        [m_Map.count_green() for location in m_sequence]
        assert m_Map.count_green.call_count == len(m_sequence)



        # def t_coordinates(start=(-181, -50), end=(181, 50), steps=20):
        # Test possible coordinates
        # Non-existent coordinates can be used, however, since the GoogleAPI will
        # respond with 'None', this error is basically treated by function t_geocoder.
        #    with raises(ValueError):
        #        t_Graph.location_sequence(start, end, steps)