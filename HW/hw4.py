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

    graph = main_rrt(xmin, xmax, ymin, ymax, start, goal, stepSize)
    a = 1