from pytest import raises
from mock import Mock, patch
import random as rd

t_Graph = Graph('London', 'Cambridge')


# FIX THAT?
def t_coordinates(start=(-181, -50), end=(181, 50), steps=20):
    # Test possible coordinates
    with raises(ValueError):
        t_Graph.location_sequence(start, end, steps)


def t_location_sequence():
    # Test calculation of location_sequence
    to_be = np.array([[-10., -10.], [-5., -5.], [0., 0.], [5., 5.], [10., 10.]])
    assert (t_Graph.location_sequence((-10, -10), (10, 10), 5) == to_be).all