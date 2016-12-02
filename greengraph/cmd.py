from argparse import ArgumentParser
from matplotlib import pyplot as plt
import greengraph.Graph as Graph


def runModule():
    parser = ArgumentParser(description='Calculates the number of green pixels between two geographical locations.')
    parser.add_argument('--begin', '-b', dest='begin', help='Enter start location.')
    parser.add_argument('--end', '-e', dest='end', help='Enter location of target destination.')
    parser.add_argument('--steps', '-s', dest='steps', help='Defines granularity of analysis, i.e. how many \'steps\' should be taken between start and destination location.')

    args = parser.parse_args()

    mygraph = Graph(args.begin, args.end)
    data = mygraph.green_between(args.steps)
    plt.plot(data)


if __name__ == '__main__':
    runModule()