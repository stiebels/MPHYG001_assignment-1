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
                with patch.object(plt, 'savefig') as m_plt_save:
                    for i in range(0,2):
                        if i == 0: # Checks functions calls if path is not specified
                            plotGraph('London', 'Cambridge', 5, path=None)
                            # Checks if plt.plot and plt.show are called exactly once per run
                            assert (m_plt_plot.call_count == 1)
                            # Checks whether plt.show is called
                            assert (m_plt_show.call_count == 1)
                            # Checks if plt.savefig is not called
                            assert (m_plt_save.call_count == 0)
                        if i == 1: # Checks function calls if path is specified
                            plotGraph('London', 'Cambridge', 5, path='/testdir/test.png')
                            # Since it's the second run in the loop, the plt.plot function should have been called twice sofar
                            assert (m_plt_plot.call_count == 2)
                            # Checks whether plt.show was called again
                            assert (m_plt_show.call_count == 1)
                            # Checks whether plt.savefig was called
                            assert (m_plt_save.call_count == 1)


def t_plotGraph_plt_input():
    # Test whether program reports ValueError when provided with no
    # input from function green_between
    with patch.object(Graph, 'green_between', return_value=None):
        with raises(ValueError):
            plotGraph('London', 'Cambridge', 5)