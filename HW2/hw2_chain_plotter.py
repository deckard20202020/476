#!/usr/bin/env python

# commented out for running without ROS
# import rospy
import matplotlib.pyplot as plt
# from cs476.msg import Chain2D


import numpy as np
import math


def get_chain_msg():
    """Return a message from the "chain_config" channel.
    This function will wait until a message is received.
    """
    # TODO: Implement this function

    # used for testing
    # msg = listener()
    # return msg

    # used with ROS
    # rospy.init_node("listener", anonymous=True)
    # msg = rospy.wait_for_message("chain_config", Chain2D)
    # return msg

    # used for running natively ROS


    # raise NotImplementedError

# def listener():
#     rospy.init_node("listener", anonymous=True)
#     msg = rospy.wait_for_message("chain_config", Chain2D)
#     return msg
    # for testing
    # callback(msg)

# def callback(msg):
#     msg_str = " ".join(map(str, msg.config))
#     rospy.loginfo(rospy.get_caller_id() + " I heard %s", msg_str)

def plot_chain(config, W, L, D):
    """Plot a 2D kinematic chain A_1, ..., A_m
    @type config: a list [theta_1, ..., theta_m] where theta_1 represents the angle between A_1 and the x-axis,
        and for each i such that 1 < i <= m, \theta_i represents the angle between A_i and A_{i-1}.
    @type W: float, representing the width of each link
    @type L: float, representing the length of each link
    @type D: float, the distance between the two points of attachment on each link
    """

    (joint_positions, link_vertices) = get_link_positions(config, W, L, D)

    fig, ax = plt.subplots()
    plot_links(link_vertices, ax)
    plot_joints(joint_positions, ax)
    ax.axis("equal")
    plt.show()


def plot_links(link_vertices, ax):
    """Plot the links of a 2D kinematic chain A_1, ..., A_m on the axis ax
    @type link_vertices: a list [V_1, ..., V_m] where V_i is the list of [x,y] positions of vertices of A_i
    """

    for vertices in link_vertices:
        x = [vertex[0] for vertex in vertices]
        y = [vertex[1] for vertex in vertices]

        x.append(vertices[0][0])
        y.append(vertices[0][1])
        ax.plot(x, y, "k-", linewidth=2)


def plot_joints(joint_positions, ax):
    """Plot the joints of a 2D kinematic chain A_1, ..., A_m on the axis ax
    @type joint_positions: a list [p_1, ..., p_{m+1}] where p_i is the position [x,y] of the joint between A_i and A_{i-1}
    """
    x = [pos[0] for pos in joint_positions]
    y = [pos[1] for pos in joint_positions]
    ax.plot(x, y, "k.", markersize=10)


def get_link_positions(config, W, L, D):
    """Compute the positions of the links and the joints of a 2D kinematic chain A_1, ..., A_m
    @type config: a list [theta_1, ..., theta_m] where theta_1 represents the angle between A_1 and the x-axis,
        and for each i such that 1 < i <= m, \theta_i represents the angle between A_i and A_{i-1}.
    @type W: float, representing the width of each link
    @type L: float, representing the length of each link
    @type D: float, the distance between the two points of attachment on each link
    @return: a tuple (joint_positions, link_vertices) where
        * joint_positions is a list [p_1, ..., p_{m+1}] where p_i is the position [x,y] of the joint between A_i and A_{i-1}
        * link_vertices is a list [V_1, ..., V_m] where V_i is the list of [x,y] positions of vertices of A_i
    """
    # # TODO: Implement this function
    # raise NotImplementedError

    cornersList = []
    jointPositionList = []

    # if m = 0, jointpositions should be an empty list
    if (len(config) == 0):
        jointPositionList = []
    else:
        jointPositionList.append([0, 0])

    # scroll through the configs calling our helper method
    for i in range(len(config)):

        # add the joints
        jointPosition = getNextJoint(i, config, W, L, D)
        jointPositionList.append(jointPosition)

    # i have a list of all the joints now
    for i in range(len(config)):
        corners = getCorners(config, i, W, L, D, jointPositionList)
        cornersList.append(corners)

    tuple = (jointPositionList, cornersList)

    # this should return a tuple
    return tuple

# will return a list of the 4 corners
def getCorners(config, i, W, L, D, jointPositionList):

    listOfPoints = []

    baseForRightVerticies = getDistToRightCorners(L, D)
    perpForTopVerticies = getPerpForTopCorners(W)
    baseForLeftVertices = getDistToLeftCorners(L, D)
    perpForBottomVerticies = getPerpForBottomBottomCorners(W)

    # is this the x, y instead of the x_t, y_t?
    # to get the x_t we need to add the x and y from the origin?
    xTopRight = baseForRightVerticies
    yTopRight = perpForTopVerticies
    # returns a list of length 2
    topRight = findNewCorner(config, i, xTopRight, yTopRight, D)

    xBottomRight = baseForRightVerticies
    yBottomRight = perpForBottomVerticies
    bottomRight = findNewCorner(config, i, xBottomRight, yBottomRight, D)

    xTopLeft = baseForLeftVertices
    yTopLeft = perpForTopVerticies
    topLeft = findNewCorner(config, i, xTopLeft, yTopLeft, D)

    xBottomLeft = baseForLeftVertices
    yBottomLeft = perpForBottomVerticies
    bottomLeft = findNewCorner(config, i, xBottomLeft, yBottomLeft, D)

    listOfPoints.append(topRight)
    listOfPoints.append(bottomRight)
    listOfPoints.append(bottomLeft)
    listOfPoints.append(topLeft)

    return listOfPoints

# will return a list of size two
def findNewCorner(config, i, x, y, D):

    theta = config[i]

    coordMatrix = buildCoordMatrix(x, y)
    # if (i == 0):
    #     translationMatrix = buildTranslationMatrix(theta, 0, 0)
    #     answerMatrix = np.dot(translationMatrix, coordMatrix)
    #     answer = [answerMatrix[0], answerMatrix[1]]
    #     return answer
    #
    # translationMatrix = buildTranslationMatrix(theta, D, 0)
    # answerMatrix = np.dot(translationMatrix, findNewCorner(config, i - 1, x, y, D))

    leftHandSide = recursion(coordMatrix, D, i, config)
    answerMatrix = np.dot(leftHandSide, coordMatrix)

    answer = [answerMatrix[0], answerMatrix[1]]
    return answer

def getNextJoint(i, config, W, L, D):

    x = 0 + D
    y = 0

    coordMatrix = buildCoordMatrix(x, y)

    leftHandSide = recursion(coordMatrix, D, i, config)
    answerMatrix = np.dot(leftHandSide, coordMatrix)

    # convert our answer to a list
    list = [answerMatrix[0], answerMatrix[1]]
    return list

def recursion(coordMatrix, D, i, listOfAngles):

    theta = listOfAngles[i]
    length = len(listOfAngles)

    if (i == 0):
        translationMatrix = buildTranslationMatrix(theta, 0, 0)
        # return np.matmul(translationMatrix, coordMatrix)
        # return np.dot(translationMatrix, coordMatrix)
        return translationMatrix

    # 0,0  d0 coordMatrix

    translationMatrix = buildTranslationMatrix(theta, D, 0)
    return np.dot(recursion(coordMatrix, D, i - 1, listOfAngles), translationMatrix)

def buildTranslationMatrix(theta, x_t, y_t):

    # matrix = ([math.cos(theta), -(math.sin(theta)), x_t],
    #           [math.sin(theta), math.cos(theta), y_t],
    #           [0, 0, 1])
    matrix = np.array([[math.cos(theta), -(math.sin(theta)), x_t], [math.sin(theta), math.cos(theta), y_t], [0, 0, 1]])

    return matrix

def buildCoordMatrix(x, y):

    matrix = np.array([x, y, 1]).reshape(-1, 1)
    # matrix = ([x, y, 1])
    return matrix

def getDistToRightCorners(L, D):
    dist = D + (L - D) / 2.0
    return dist

def getPerpForTopCorners(W):
    return W / 2.0

def getDistToLeftCorners(L, D):
    dist = -((L - D) / 2)
    return dist

def getPerpForBottomBottomCorners(W):
    return -(W / 2.0)


if __name__ == "__main__":

    # used for running with ROS
    # chain = get_chain_msg()
    # plot_chain(chain.config, chain.W, chain.L, chain.D)

    # used for running natively
    # 0.7853981633974483
    # 1.5707963267948966 - 0.7853981633974483 - W
    # 2 - L
    # 12 - D
    # 10

    config = [0.7853981633974483,
    1.5707963267948966, - 0.7853981633974483]
    W = 2
    L = 12
    D = 10

    plot_chain(config, W, L, D)