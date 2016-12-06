from mock import Mock, patch, MagicMock
import numpy as np
from greengraph.Map import Map
from PIL import Image


directory = '/home/sist/PycharmProjects/MPHYG001_assignment-1/greengraph/tests/fixtures/'
m_img = Image.open(directory + 'london_map.png')
m_green = Image.open(directory + 'green.png')


# INVALID PNG HEADER ???
@patch('requests.get', return_value=MagicMock(content=m_img.tobytes()))
def t_Map(m_req_get):
    for i in range(0, 2):
        if i == 0:
            t_Map = Map(-10, -10, satellite=False)

            # Check if requests.get is called with right parameters
            m_req_get.assert_called_with(
                base="http://maps.googleapis.com/maps/api/staticmap?",
                params=dict(
                    sensor=str(False).lower(),
                    zoom=10,
                    size="x".join(map(str, (400, 400))),
                    center=",".join(map(str, (-10, -10))),
                    style="feature:all|element:labels|visibility:off"
                )
            )
        else:
            t_Map = Map(-10, -10)
            # Check if requests.get is called with right parameters
            m_req_get.assert_called_with(
                base="http://maps.googleapis.com/maps/api/staticmap?",
                params=dict(
                    sensor=str(False).lower(),
                    zoom=10,
                    size="x".join(map(str, (400, 400))),
                    center=",".join(map(str, (-10, -10))),
                    style="feature:all|element:labels|visibility:off",
                    maptype = "satellite"
            )
            )

            # Check self.pixels calculation
            assert (type(t_Map.pixels) is 'numpy.ndarray')
            assert (len(t_Map.pixels) == 400)
            assert (np.shape(t_Map.pixels) == (400, 400, 3))


# INVALID PNG HEADER ???
@patch('requests.get', return_value=MagicMock(content=m_img.tobytes()))
def t_green(m_req_get):
    t_Map = Map(-10, -10)

    # Check that green is recognized/computed correctly
    thresholds = range(0, 10)
    check_green = np.array
    for number in thresholds:
        check_green.append(sum(sum(t_Map.green(number))))

    for i in range(1, len(check_green)):
        assert ((check_green[i] > check_green[i - 1]) is True)


# INVALID PNG HEADER ???
@patch('requests.get', return_value=MagicMock(content=m_green.tobytes()))
def t_count_green(m_req_get):
    t_Map = Map(-10, -10)

    # Check that green and count_green return correct sum
    # REPLACE X with NUMBER OF GREEN PIXELS
    assert (t_Map.count_green(1.1) == XXX)
    assert (sum(sum(t_Map.green(1.1))) == XXX)