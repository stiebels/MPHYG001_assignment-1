from io import StringIO
from io import BytesIO
import numpy as np
from matplotlib import image as img
import requests
from pytest import raises
from mock import Mock, patch, MagicMock
import numpy as np
import geopy
from greengraph.Graph import Graph
from greengraph.Map import Map
import os, sys
from PIL import Image


directory = '/home/sist/PycharmProjects/MPHYG001_assignment-1/greengraph/tests/fixtures/'
m_img = Image.open(directory + 'london_map.png')


# INVALID PNG HEADER ???
@patch('requests.get', return_value=MagicMock(content=m_img.tobytes()))
def t_Map(m_req_get):
    t_Map = Map(-10, -10)

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

    # Check self.pixels calculation
    assert (type(t_Map.pixels) is numpy.ndarray)
    assert (len(t_Map.pixels) == 400)
    assert (np.shape(t_Map.pixels) == (400, 400, 3))