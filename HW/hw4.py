from matplotlib import pyplot as plt, patches
import numpy as np

from HW.planning import Planning
from HW.vertex import Vertex


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

import math


def draw(ax, cspace, obstacles, qI, qG, G, path, title=""):
    """Plot the C-space, obstacles, qI, qG, and graph on the axis ax
    @type ax: axes.Axes, created, e.g., fig, ax = plt.subplots()
    @type cspace: a list [(xmin, xmax), (ymin, ymax)] indicating that the C-space
        is given by [xmin, xmax] \times [ymin, ymax].
    @type G: an object with draw(ax) method. This object represents a graph to be drawn.
    @type obstacles: a list [obs_1, ..., obs_m] of obstacles, where obs_i is a list of coordinates
        on the boundary of the i^{th} obstacle.
    @type qI: a tuple (x, y), indicating the initial configuration.
    @type qG: a tuple (x, y), indicating the goal configuration
    @type path: a list of tuples specifying the sequence of configurations visited along the path
    @type title: a string, indicating the title of the plot
    """

    draw_cspace(ax, cspace, obstacles)
    drawG = getattr(G, "draw", None)
    if callable(drawG):
        G.draw(ax)
    if qI is not None:
        if len(qI) == 2:
            ax.plot(qI[0], qI[1], "bx", markersize=10)
        elif len(qI) == 3:
            ax.plot(
                qI[0],
                qI[1],
                marker=(3, 0, qI[2] * 180 / math.pi - 90),
                markersize=15,
                linestyle="None",
                markerfacecolor="blue",
                markeredgecolor="blue",
            )
    if qG is not None:
        if len(qI) == 2:
            ax.plot(qG[0], qG[1], "bo", markersize=10)
        elif len(qG) == 3:
            ax.plot(
                qG[0],
                qG[1],
                marker=(3, 0, qG[2] * 180 / math.pi - 90),
                markersize=15,
                linestyle="None",
                markerfacecolor="red",
                markeredgecolor="red",
            )
    if len(path) > 0:
        ax.plot(
            [state[0] for state in path],
            [state[1] for state in path],
            "b-",
            linewidth=5,
        )
    if len(title) > 0:
        ax.set_title(title, fontsize=20)


def draw_cspace(ax, cspace, obstacles, tick_step=[1, 1]):
    """Draw the C-space and C-space obstacles on the axis ax
    @type cspace: a list [(xmin, xmax), (ymin, ymax)] indicating that the C-space
        is given by [xmin, xmax] \times [ymin, ymax].
    @type obstacles: a list [obs_1, ..., obs_m] of obstacles, where obs_i is a list of coordinates
        on the boundary of the i^{th} obstacle.
    """
    for obs in obstacles:
        ax.plot([v[0] for v in obs], [v[1] for v in obs], "r-", linewidth=3)

    ax.set_xticks(
        range(math.ceil(cspace[0][0]), math.floor(cspace[0][1]) + 1, tick_step[0])
    )
    ax.set_yticks(
        range(math.ceil(cspace[1][0]), math.floor(cspace[1][1]) + 1, tick_step[1])
    )
    ax.set(xlim=cspace[0], ylim=cspace[1])
    ax.set_aspect("equal", adjustable="box")
    ax.tick_params(axis="x", labelsize=20)
    ax.tick_params(axis="y", labelsize=20)


# def printResults(obstacles: list):
def printResults(xmin, xmax, ymin, ymax, graph, obstacles, start, goal, dt):
    # x1, y1 = obstacles[0].exterior.xy
    # x2, y2 = obstacles[1].exterior.xy
    # print()

    # fig = plt.figure(figsize=(60, 10))
    fix, ax = plt.subplots(figsize=(60,10))

    # plt.plot(x1, y1)
    # plt.plot(x2, y2)

    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)

    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

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

    # plot each verticies
    for v in graph.get_vertices():
        x1 = v.x
        y1 = v.y
        if v == goal:
            plt.plot(x1, y1, 'bx')
        elif v == start:
            plt.plot(x1, y1, 'bo')
        else:
            plt.plot(x1, y1, 'ko')


    # plot all the edged
    for e in graph.get_edges():
        first = [e.vertex1.x, e.vertex2.x]
        second = [e.vertex1.y, e.vertex2.y]
        ax.plot(first, second, color='k')

    # # make the start a blue dot
    # plt.plot(start.x, start.y, 'bo')
    #
    # # make the goal a blue x
    # plt.plot(goal.x, goal.y, 'bx')



    plt.show()

def main_rrt(xmin, xmax, ymin, ymax, start, goal, stepSize):
    # TODO: implement main_rrt in hw4
    plan = Planning(xmin, xmax, ymin, ymax, start, goal, stepSize)
    graph = plan.RRT()
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

    graph = main_rrt(xmin, xmax, ymin, ymax, start, goal, stepSize)

    obstacles = None
    printResults(xmin, xmax, ymin, ymax, graph, obstacles, start, goal, dt)