from matplotlib import pyplot as plt, patches
import numpy as np

from HW.edge import Edge
from HW.planning import Planning
from HW.vertex import Vertex
import math


def parse_args():
    # TODO: implement parse_args in hw4
    raise NotImplementedError
    # """Parse command line arguments"""
    # parser = argparse.ArgumentParser(description="Run forward search")
    # parser.add_argument(
    #     "desc",
    #     metavar="problem_description_path",
    #     type=str,
    #     help="path to the problem description file containing the grid configuration, the initial cell, and the goal region",
    # )
    # parser.add_argument(
    #     "--alg",
    #     choices=[ALG_BFS, ALG_DFS, ALG_ASTAR],
    #     required=False,
    #     default=ALG_BFS,
    #     dest="alg",
    #     help="search algorithm, default to bfs",
    # )
    # parser.add_argument(
    #     "--out",
    #     metavar="output_path",
    #     type=str,
    #     required=False,
    #     default="",
    #     dest="out",
    #     help="path to the output file",
    # )
    #
    # args = parser.parse_args(sys.argv[1:])
    # if not args.out:
    #     args.out = (
    #             os.path.splitext(os.path.basename(args.desc))[0] + "_" + args.alg + ".json"
    #     )
    #
    # print("Problem description: ", args.desc)
    # print("Search algorithm:    ", args.alg)
    # print("Output:              ", args.out)
    #
    # return args


# def printResults(obstacles: list):
def printResults(xmin, xmax, ymin, ymax, graph, start, goal, dt):
    # fig = plt.figure(figsize=(60, 10))
    # fix, ax = plt.subplots(figsize=(60,10))


    # set up the circle parameters
    circle1_center = [0, 1]
    circle2_center = [0, -1]
    circle_radius = 1 - dt

    # set up the x and y values for the circles
    t = np.linspace(0, np.pi, 1000)
    x1 = circle1_center[0] + circle_radius * np.cos(t)
    y1 = circle1_center[1] + circle_radius * -np.sin(t)
    x2 = circle2_center[0] + circle_radius * np.cos(t)
    y2 = circle2_center[1] + circle_radius * np.sin(t)

    # create the plot
    fig, ax = plt.subplots()
    ax.set_xlim([xmin, xmax])
    ax.set_ylim([ymin, ymax])

    # plot the circles
    ax.plot(x1, y1, color='red')
    ax.plot(x2, y2, color='red')

    # plot each vertex
    for v in graph.get_vertices():
        x1 = v._x
        y1 = v._y
        if v == goal:
            ax.plot(x1, y1, 'bx')
        elif v == start:
            ax.plot(x1, y1, 'bo')
        else:
            ax.plot(x1, y1, 'ko')

    # make sure to plot the goal
    # used for testing while reducing dt down to 0
    ax.plot(goal._x, goal._y, 'bx')

    # plot all the edges
    for e in graph.get_edges():
        first = [e.vertex1._x, e.vertex2._x]
        second = [e.vertex1._y, e.vertex2._y]
        ax.plot(first, second, color='k')

    plt.show()

def printResultsWithPath(xmin, xmax, ymin, ymax, graph, start, goal, dt):
    # fig = plt.figure(figsize=(60, 10))
    # fix, ax = plt.subplots(figsize=(60,10))


    # set up the circle parameters
    circle1_center = [0, 1]
    circle2_center = [0, -1]
    circle_radius = 1 - dt

    # set up the x and y values for the circles
    t = np.linspace(0, np.pi, 1000)
    x1 = circle1_center[0] + circle_radius * np.cos(t)
    y1 = circle1_center[1] + circle_radius * -np.sin(t)
    x2 = circle2_center[0] + circle_radius * np.cos(t)
    y2 = circle2_center[1] + circle_radius * np.sin(t)

    # create the plot
    fig, ax = plt.subplots()
    ax.set_xlim([xmin, xmax])
    ax.set_ylim([ymin, ymax])

    # plot the circles
    ax.plot(x1, y1, color='red')
    ax.plot(x2, y2, color='red')

    # plot each vertex
    for v in graph.get_vertices():
        x1 = v._x
        y1 = v._y
        if v == goal:
            ax.plot(x1, y1, 'bx')
        elif v == start:
            ax.plot(x1, y1, 'bo')
        else:
            ax.plot(x1, y1, 'ko')

    # make sure to plot the goal
    # used for testing while reducing dt down to 0
    ax.plot(goal._x, goal._y, 'bx')

    # plot all the edges
    for e in graph.get_edges():
        first = [e.vertex1._x, e.vertex2._x]
        second = [e.vertex1._y, e.vertex2._y]
        ax.plot(first, second, color='k')

    # plot the path
    # find the goal in the graph
    goalVertex = None
    for v in graph.get_vertices():
        if v == goal:
            goalVertex = v
            break

    while goalVertex._parent is not None:
        #make the goalVertex blue
        x1 = goalVertex._x
        y1 = goalVertex._y
        ax.plot(x1, y1, 'bo')

        # plot the edge in blue
        edge = Edge(goalVertex, goalVertex._parent)
        first = [edge.vertex1._x, edge.vertex2._x]
        second = [edge.vertex1._y, edge.vertex2._y]
        ax.plot(first, second, color='b')

        # reassign the goalVertex
        goalVertex = goalVertex._parent

    plt.show()

def main_rrtExplorationWithoutCollision(xmin, xmax, ymin, ymax, start, goal, stepSize, dt):
    plan = Planning(xmin, xmax, ymin, ymax, start, goal, stepSize, dt)
    graph = plan.RRTExplorationWithoutCollision()
    return graph

def main_rrtExplorationWithCollision(xmin, xmax, ymin, ymax, start, goal, stepSize, dt):
    plan = Planning(xmin, xmax, ymin, ymax, start, goal, stepSize, dt)
    graph = plan.RRTExplorationWithCollision()
    return graph

def main_rrtPathFindingWithCollision(xmin, xmax, ymin, ymax, start, goal, stepSize, dt):
    plan = Planning(xmin, xmax, ymin, ymax, start, goal, stepSize, dt)
    graph = plan.RRTPathfindingWithCollision()
    return graph

def main_prm():
    # TODO: implement main_prm in hw4
    raise NotImplementedError

if __name__ == "__main__":
    # input is just the algorithm RRT or PRM
    # output should be the picture
    xmin = -3
    xmax = 3
    ymin = -1
    ymax = 1
    start = Vertex(-2, -0.5)
    goal = Vertex(2, -0.5)
    stepSize = .1
    dt = .1

    # explorationGraphWithoutCollision = main_rrtExplorationWithoutCollision(xmin, xmax, ymin, ymax, start, goal, stepSize, dt)
    # printResults(xmin, xmax, ymin, ymax, explorationGraphWithoutCollision, start, goal, dt)

    explorationGraphWithCollision = main_rrtExplorationWithCollision(xmin, xmax, ymin, ymax, start, goal, stepSize, dt)
    printResults(xmin, xmax, ymin, ymax, explorationGraphWithCollision, start, goal, dt)

    # pathFindingWithCollision = main_rrtPathFindingWithCollision(xmin, xmax, ymin, ymax, start, goal, stepSize, dt)
    # printResultsWithPath(xmin, xmax, ymin, ymax, pathFindingWithCollision, start, goal, dt)

    # just run all three.
