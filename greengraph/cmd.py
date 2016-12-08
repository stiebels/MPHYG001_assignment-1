from argparse import ArgumentParser
from matplotlib import pyplot as plt
from greengraph.Graph import Graph


def runModule():
    parser = ArgumentParser(description='Calculates the number of green pixels between two geographical locations.')
    parser.add_argument('--begin', '-b', dest='begin', help='Enter start location.', required=True)
    parser.add_argument('--end', '-e', dest='end', help='Enter location of target destination.', required=True)
    parser.add_argument('--steps', '-s', default=25, dest='steps',
                        help='Steps/points between begin and end', required=False)

    args = parser.parse_args()

    mygraph = Graph(args.begin, args.end)
    data = mygraph.green_between(args.steps)
    plt.plot(data)


if __name__ == '__main__':
    runModule()