from argparse import ArgumentParser
from matplotlib import pyplot as plt
from greengraph.Graph import Graph


def runModule():
    parser = ArgumentParser(description='Calculates the number of green pixels between two geographical locations.')
    parser.add_argument('-b', dest='begin', help='Enter start location.', required=True)
    parser.add_argument('-e', dest='end', help='Enter location of target destination.', required=True)
    parser.add_argument('-s', default=25, dest='steps', help='Steps between begin and end', required=False)

    args = parser.parse_args()
    plotGraph(args.begin, args.end, args.steps)

def plotGraph(begin, end, steps):
    mygraph = Graph(begin, end)
    data = mygraph.green_between(steps)
    plt.plot(data)


if __name__ == '__main__':
    runModule()