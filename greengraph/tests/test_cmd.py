from pytest import raises
from mock import patch
from greengraph.Graph import Graph
from matplotlib import pyplot as plt
from greengraph.cmd import plotGraph


'''
This class tests the plotting functions in cmd.
'''

def t_plotGraph_plt():
    # Test calling of plotting functions in final graph
    with patch.object(Graph, 'green_between') as m_green_between:
        with patch.object(plt, 'plot') as m_plt_plot:
            with patch.object(plt, 'show') as m_plt_show:
                plotGraph('London', 'Cambridge', 5)

                # Checks if plt functions are called exactly once per run
                assert (m_plt_plot.call_count == 1)
                assert (m_plt_show.call_count == 1)


def t_plotGraph_plt_input():
    # Test whether program reports ValueError when provided with no
    # input from function green_between
    with patch.object(Graph, 'green_between', return_value=None):
        with raises(ValueError):
            plotGraph('London', 'Cambridge', 5)