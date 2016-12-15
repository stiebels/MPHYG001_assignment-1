from argparse import ArgumentParser
from matplotlib import pyplot as plt
from greengraph.Graph import Graph

'''
This class implements the command line interface.
'''

def runModule():
    parser = ArgumentParser(description='Generates a graph that displays the number of green pixels per step between two geographical locations.')
    parser.add_argument(dest='begin', help='Enter start location, e.g. \'London\'.')
    parser.add_argument(dest='end', help='Enter location of target destination, e.g. \'Cambridge\'.')
    parser.add_argument('-s', default=25, dest='steps', help='Steps between begin and end, e.g. \'10\'.', required=False)
    parser.add_argument('-p', default=None, dest='path', help='If specified, graph is saved to location specified here, e.g. \'/home/user/graph.png\'. Otherwise, graph is only displayed but not auto-saved.', required=False)


    args = parser.parse_args()
    plotGraph(args.begin, args.end, args.steps, args.path)


def plotGraph(begin, end, steps, path):
    mygraph = Graph(begin, end)
    data = mygraph.green_between(steps)
    plt.plot(data)
    if path:
        plt.savefig(path)
    else:
        plt.show()


if __name__ == '__main__':
    runModule()