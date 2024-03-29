import json, sys, os, argparse, math
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
import matplotlib.pyplot as plt
import numpy

from planning import (
    rrt,
    prm,
    StraightEdgeCreator,
    EuclideanDistanceComputator,
    EmptyCollisionChecker,
    ObstacleCollisionChecker, PolygonCollisionChecker,
)
from obstacle import construct_circular_obstacles, WorldBoundary2D, construct_polygon_obstacles
from draw_cspace import draw

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
    xG = tuple(data["xG"])
    # U = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    # return (O, W, L, D, xI, XG, U)
    return (O, W, L, D, xI, xG)

def main_rrt(
    cspace, qI, qG, edge_creator, distance_computator, collision_checker, obs_boundaries
):
    """Task 1 (Exploring the C-space using RRT) and Task 2 (Solve the planning problem using RRT)"""
    # fig, (ax1, ax2, ax3) = plt.subplots(3, 1)

    # # Task 1a: Neglect obstacles and goal
    # title1 = "RRT exploration, neglecting obstacles"
    # (G1, _, _) = rrt(
    #     cspace=cspace,
    #     qI=qI,
    #     qG=None,
    #     edge_creator=edge_creator,
    #     distance_computator=distance_computator,
    #     collision_checker=EmptyCollisionChecker(),
    # )
    # draw(ax1, cspace, obs_boundaries, qI, qG, G1, [], title1)
    #
    # # Task 1b: Include obstacles, neglect goal
    # title2 = "RRT exploration, considering obstacles"
    # (G2, _, _) = rrt(
    #     cspace=cspace,
    #     qI=qI,
    #     qG=None,
    #     edge_creator=edge_creator,
    #     distance_computator=distance_computator,
    #     collision_checker=collision_checker,
    # )
    # draw(ax2, cspace, obs_boundaries, qI, qG, G2, [], title2)

    # Task 2: Include obstacles and goal
    title3 = "RRT planning"
    (G3, root3, goal3) = rrt(
        cspace=cspace,
        qI=qI,
        qG=qG,
        edge_creator=edge_creator,
        distance_computator=distance_computator,
        collision_checker=collision_checker,
    )
    path = []
    if goal3 is not None:
        path = G3.get_path(root3, goal3)
    draw(ax, cspace, obs_boundaries, qI, qG, G3, path, title3)

    plt.show()

if __name__ == "__main__":
    args = parse_args()
    (O, W, L, D, xI, xG) = parse_desc(args.desc)

    # our cspace is (-pi, pi)
    cspace = [(-numpy.pi, numpy.pi), (-numpy.pi, numpy.pi)]

    # construct our obstacles
    obstacles = construct_polygon_obstacles(O)

    edge_creator = StraightEdgeCreator(0.1)
    distance_computator = EuclideanDistanceComputator()
    collision_checker = PolygonCollisionChecker(W, L, D, obstacles)


    # for i in range(10):
    title3 = "RRT planning"
    (G3, root3, goal3) = rrt(
        cspace=cspace,
        qI=xI,
        qG=xG,
        edge_creator=edge_creator,
        distance_computator=distance_computator,
        collision_checker=collision_checker,
    )
    path = []
    fig,ax=plt.subplots()
    if goal3 is not None:
        path = G3.get_path(root3, goal3)
    draw(ax, cspace, O, xI, xG, G3, path, title3)

    plt.show()

    # output results to output file
    #my tree is called G3

    #all the vertices
    # "vertices": [{"id": 0, "config": [1.0471975511965976, 0.5235987755982988]}, ...
    # list of dictionaries with 2 keys
    vertexList = []
    for v in G3.vertices:
        vertexDictionary = {}
        vertexDictionary["id"] = v
        vertexDictionary["config"] = [G3.vertices[v][0], G3.vertices[v][1]]
        vertexList.append(vertexDictionary)

    #all the edges
    edgesList = []
    # "edges": [[0, 2], [2, 1], ...
    for e in G3.edges:
        # make a list from the tuple
        list = []
        list.append(e[0])
        list.append(e[1])
        edgesList.append(list)

    # create the path if there is one
    # "path": [0, 2, 4, 10, 11, 13]
    # don't forget to add them backwards
    path = []

    goalVertex = -1
    # find the goal vertex
    for v in G3.vertices.items():
        # returns list of (key,value)
        if v[1][0] == xG[0] and v[1][1] == xG[1]:
            goalVertex = v[1]
            indexOfGoalVertex = v[0]
            path.append(indexOfGoalVertex)

    # if we have found a goal
    if len(path) > 0:
        currentVertexIndex = path[0]
        lengthOfParents = len(G3.parents[currentVertexIndex])
        while lengthOfParents > 0:
            #find the parent
            parent = G3.parents[currentVertexIndex][0]
            path.insert(0, parent)
            currentVertexIndex = parent
            lengthOfParents = len(G3.parents[currentVertexIndex])

    # taken from https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/#
    outputInfo = {
        "vertices": vertexList,
        "edges": edgesList,
        "path": path
    }

    # Serializing json
    json_object = json.dumps(outputInfo, indent=4)

    # Writing to sample.json
    with open("midterm_out.json", "w") as outfile:
        outfile.write(json_object)
