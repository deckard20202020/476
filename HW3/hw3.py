import json, sys, os, argparse
import math

# import matplotlib.pyplot as plt
# # from discrete_search import fsearch, ALG_BFS
# from HW1.discrete_search import fsearch, ALG_BFS
# # from hw1 import Grid2DStates, GridStateTransition, Grid2DActions, draw_path
# from HW1.hw1 import Grid2DStates, GridStateTransition, Grid2DActions, draw_path
from HW2.hw2_chain_plotter import get_link_positions

from shapely.geometry import Polygon


LINK_ANGLES = [i - 180 for i in range(360)]


def compute_Cobs(O, W, L, D):
# def compute_Cobs():
    """Compute C-Space obstacles for a 2-link robot
    @type O:   a list of obstacles, where for each i, O[i] is a list [(x_0, y_0), ..., (x_m, y_m)]
               of coordinates of the vertices of the i^th obstacle
    @type W:   float, representing the width of each link
    @type L:   float, representing the length of each link
    @type D:   float, the distance between the two points of attachment on each link
    @return: a list of configurations (theta_1, theta_2) of the robot that leads to a collision
        between the robot and an obstacle in O.
    """
    # # TODO: Implement this function
    # raise NotImplementedError

    configurationList = []

    # create the 360 x 360 grid
    rows, cols = (360, 360)
    grid = [[0] * cols] * rows
    for i in range(360):
        for j in range(360):
            grid[i][j] = [i - 180, j - 180]

    # # scroll through the 360 x 360 grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # find the link positions of the robot
            config = grid[i][j]
            radiansConfig = [math.radians(config[0]), math.radians(config[1])]
    #         config = [math.pi/2.0, 0]
            tuple = get_link_positions(radiansConfig, W, L, D)
            linkPositions = tuple[1]

            # scroll through the obstacles
            for k in range(len(O)):
                obstacle = O[k]
                # scroll through the link positions
                for l in range(len(linkPositions)):

                    link = linkPositions[l]
                    # p1 = Polygon([(0, 0), (1, 1), (1, 0)])
                    # p2 = Polygon([(0, 1), (1, 0), (1, 1)])
                    p1 = Polygon(link)
                    p2 = Polygon(obstacle)
                    doesIntersect = p1.intersects(p2)

                    # if they collide add this to our list of bad configurations
                    if(doesIntersect == True):
                        configurationList.append(grid[i][j])


    return configurationList


def compute_Cfree(Cobs):
    """Compute the free space for a 2-link robot
    @type Cobs: a list of configurations (theta_1, theta_2) of the robot that leads to a collision
                between the robot and an obstacle in O.
    @return an instance of Grid2DStates that represents the free space
    """
    # TODO: Implement this function
    raise NotImplementedError

# This function should return an instance of Grid2DStates class from Homework 1


def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description="Run forward search")
    parser.add_argument(
        "desc",
        metavar="problem_description_path",
        type=str,
        help="path to the problem description file containing the obstacle region in the world as well as the size and shape of the robot, including the width and length of each link, and the distance between two points of attachment",
    )
    parser.add_argument(
        "--out",
        metavar="output_path",
        type=str,
        required=False,
        default="",
        dest="out",
        help="path to the output file",
    )

    args = parser.parse_args(sys.argv[1:])
    if not args.out:
        args.out = os.path.splitext(os.path.basename(args.desc))[0] + "_out" + ".json"

    print("Problem description: ", args.desc)
    print("Output:              ", args.out)

    return args


def parse_desc(desc):
    """Parse problem description json file to get the problem description"""
    with open(desc) as desc:
        data = json.load(desc)

    O = data["O"]
    W = data["W"]
    L = data["L"]
    D = data["D"]
    xI = tuple(data["xI"])
    XG = [tuple(x) for x in data["XG"]]
    U = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    return (O, W, L, D, xI, XG, U)


if __name__ == "__main__":
    # args = parse_args()
    # (O, W, L, D, xI, XG, U) = parse_desc(args.desc)
    # Cobs = compute_Cobs(O, W, L, D)
    #
    # X = compute_Cfree(Cobs)
    # f = GridStateTransition()
    # U = Grid2DActions(X, f)
    #
    # search_result = fsearch(X, U, f, xI, XG, ALG_BFS)
    #
    # result = {"Cobs": Cobs, "path": search_result["path"]}
    #
    # with open(args.out, "w") as outfile:
    #     json.dump(result, outfile)
    #
    # fig, ax = plt.subplots()
    # X.draw(ax, grid_on=False, tick_step=[30, 30])
    # draw_path(ax, search_result["path"])
    # plt.show()

    # me testing
    O = [[[-1, -13], [1, -13], [ 1, -11], [-1, -11]], [[-1, 11], [ 1, 11], [ 1, 13], [-1, 13]]]

    W = 2
    L = 12
    D = 10
    xI = [60, 30]
    XG = [60, 150]

    p1 = Polygon([(0, 0), (1, 1), (1, 0)])
    p2 = Polygon([(0, 1), (1, 0), (1, 1)])

    listOfCollisions = compute_Cobs(O, W, L, D)
    print(listOfCollisions)