from mock import Mock, patch, MagicMock
import numpy as np
from PIL import Image
import os
from io import BytesIO
from greengraph.Map import Map


def define_img_fixtures():
    directory = '/home/sist/PycharmProjects/MPHYG001_assignment-1/greengraph/tests/fixtures/'
    m_imgs_fix = []

    for file in os.listdir(directory):
        byteImgIO = BytesIO()
        m_img = Image.open(directory + str(file))
        m_img.save(byteImgIO, "PNG")
        byteImgIO.seek(0)
        m_imgs_fix.append(byteImgIO.read())

    return m_imgs_fix


@patch('requests.get', return_value=MagicMock(content=define_img_fixtures()[0]))
def t_Map_init(m_req_get):
    for i in range(0, 2):
        if i == 0:
            t_Map = Map(51.5073509, -0.1277583, satellite=False)  # London

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

            # Check self.pixels calculation
            assert (str(type(t_Map.pixels)) == '<class \'numpy.ndarray\'>')
            assert (len(t_Map.pixels) == 400)
            assert (np.shape(t_Map.pixels) == (400, 400, 3))


@patch('requests.get', return_value=MagicMock(content=define_img_fixtures()[0]))
def t_green(m_req_get):
    t_Map = Map(51.5073509, -0.1277583)  # London

    # Check that green is recognized/computed correctly
    thresholds = np.arange(0.5, 2.5, 0.5)
    check_green = []
    for number in thresholds:
        check_green.append(sum(sum(t_Map.green(number))))

    for i in range(1, len(check_green)):
        assert ((check_green[i] < check_green[i - 1]) == True)


@patch('requests.get', return_value=MagicMock(content=define_img_fixtures()[0]))
def t_count_green(m_req_get):
    t_Map = Map(51.5073509, -0.1277583)  # London

    # Check that green and count_green return correct sums
    assert (t_Map.count_green(1.1) == 108024)
    assert (sum(sum(t_Map.green(1.1))) == 108024)


@patch('requests.get', return_value=MagicMock(content=define_img_fixtures()[0]))
def t_show_green(m_req_get):
    t_Map = Map(51.5073509, -0.1277583)  # London

    # Checking decoding of PNG map by randomly checking coloring of PNG map
    zeros = 0
    nines = 0
    for char in t_Map.show_green(t_Map):
        if '0' in str(char):
            zeros += 1
        if '9' in str(char):
            nines += 1

    assert (zeros == 3958)
    assert (nines == 3583)

    # Checking size and type of output of function
    assert (len(t_Map.show_green(t_Map)) == 22283)
    assert (str(type(t_Map.show_green(t_Map))) == '<class \'bytes\'>')