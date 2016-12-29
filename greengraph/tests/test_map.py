from mock import patch, MagicMock
import numpy as np
from PIL import Image
import os
from io import BytesIO
from greengraph.Map import Map
import pickle


'''
This class tests the class Map and its functions.
'''


def load_img_fixtures():
    # Loads a 400x400px map of London as PNG
    # which is used as fixture for offline testing

    directory = str(os.path.dirname(os.path.abspath(__file__)) + '/fixtures/')
    byteImgIO = BytesIO()
    m_img_fix = Image.open(directory + str('lc1.png'))
    m_img_fix.save(byteImgIO, "PNG")
    byteImgIO.seek(0)
    m_img_fix = byteImgIO.read()
    return m_img_fix


def load_map_fixtures():
    # Loads a predefined Map object of London as fixture for offline testing.
    # Map(51.5073509, -0.1277583)

    directory = str(os.path.dirname(os.path.abspath(__file__)) + '/fixtures/')
    file = open(directory+"mock_map",'rb')
    m_Map_fix = pickle.load(file)
    file.close()
    return m_Map_fix


@patch('requests.get', return_value=MagicMock(content=load_img_fixtures()))
def test_Map_init(m_req_get):
    # Tests the parameter initialization and creation of a Map object

    for i in range(0, 2):
        if i == 0:
            t_Map = Map(51.5073509, -0.1277583, satellite=False)
            # Check if requests.get is called with right parameters
            m_req_get.assert_called_with(
                "http://maps.googleapis.com/maps/api/staticmap?",
                params=dict(
                    sensor=str(False).lower(),
                    zoom=10,
                    size="x".join(map(str, (400, 400))),
                    center=",".join(map(str, (51.5073509, -0.1277583))),  # London
                    style="feature:all|element:labels|visibility:off"
                )
            )

        else:
            t_Map = Map(51.5073509, -0.1277583)  # London
            # Check if requests.get is called with right parameters
            m_req_get.assert_called_with(
                "http://maps.googleapis.com/maps/api/staticmap?",
                params=dict(
                    sensor=str(False).lower(),
                    zoom=10,
                    size="x".join(map(str, (400, 400))),
                    center=",".join(map(str, (51.5073509, -0.1277583))),  # London
                    style="feature:all|element:labels|visibility:off",
                    maptype="satellite"
                )
            )

        # Check calculation of pixels
        assert (str(type(t_Map.pixels)) == str(type(load_map_fixtures().pixels)))
        assert (len(t_Map.pixels) == len(load_map_fixtures().pixels))
        assert (np.shape(t_Map.pixels) == np.shape(load_map_fixtures().pixels))
    # Check if requests.get is executed once per object creation
    assert (m_req_get.call_count == 2)


@patch('requests.get', return_value=MagicMock(content=load_img_fixtures()))
def test_green(m_req_get):
    # Tests the correctness of the computation done by this function.

    t_Map = Map(51.5073509, -0.1277583)

    # Check that green is recognized/computed correctly
    thresholds = np.arange(0.5, 2.5, 0.5)
    check_green = []
    for i in range(0, len(thresholds)):
        check_green.append(sum(sum(t_Map.green(thresholds[i]))))
        # Compares computation of t_Map.green() to calculation of fixture
        assert (check_green[i] == sum(sum(load_map_fixtures().green(thresholds[i]))))

    for i in range(1, len(check_green)):
        # Checks whether an increasing threshold has the expected effect
        # on the outcome
        assert ((check_green[i] < check_green[i - 1]) == True)


@patch('requests.get', return_value=MagicMock(content=load_img_fixtures()))
def test_count_green(m_req_get):
    # Tests whether the computation done by this functions is correct
    # and matches the manual computation (sum(sum(x))) of the green() function.

    t_Map = Map(51.5073509, -0.1277583)

    # Check that count_green returns correct value
    assert ((t_Map.count_green(1.1) == load_map_fixtures().count_green(1.1)))
    assert (t_Map.count_green(1.1) == (sum(sum(t_Map.green(1.1)))))


@patch('requests.get', return_value=MagicMock(content=load_img_fixtures()))
def test_show_green(m_req_get):
    # Tests the decoding of the PNG file and the correctness
    # of the return value.

    t_Map = Map(51.5073509, -0.1277583)

    # Checking decoding of PNG map by comparing to fixture
    assert(load_map_fixtures().show_green(t_Map) ==
           t_Map.show_green(t_Map))

    # Checking size and type of output of function
    assert (len(t_Map.show_green(t_Map)) ==
            len(load_map_fixtures().show_green(t_Map)))
    assert (str(type(t_Map.show_green(t_Map))) ==
            str(type(load_map_fixtures().show_green(t_Map))))