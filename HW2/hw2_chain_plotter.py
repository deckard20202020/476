#!/usr/bin/env python
import rospy
import matplotlib.pyplot as plt
from cs476.msg import Chain2D
import numpy as np
import math


def get_chain_msg():
    """Return a message from the "chain_config" channel.
    This function will wait until a message is received.
    """
    # TODO: Implement this function
    # are we just trying to set up a node to listen for the message
    # that was published by hw2_chain_configurator?
    listener()
    # raise NotImplementedError

def listener():
    rospy.init_node("listener", anonymous=True)
    msg = rospy.wait_for_message("chain_config", Chain2D)
    return msg
    # for testing
    # callback(msg)

def callback(msg):
    msg_str = " ".join(map(str, msg.config))
    rospy.loginfo(rospy.get_caller_id() + " I heard %s", msg_str)

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

    # initialize joint position to 0,0
    jointPosition = [0,0]

    cornersList = []
    jointPositionList = []

    # if m = 0, jointpositions should be an empty list
    if (len(config) == 0):
        jointPositionList = []
    else:
        jointPositionList.append([0, 0])

    answer = []

    # scroll through the configs calling our helper method
    for i in range(len(config)):
        theta = config[i]

        # add the corners
        corners = getCorners(theta, W, L, D, jointPosition)
        cornersList.append(corners)

        # add the joints
        jointPosition = getNextJoint(theta, W, L, D, jointPosition)
        jointPositionList.append(jointPosition)

    tuple = (jointPositionList, cornersList)

    # this should return a tuple
    return tuple

# will return a list of the 4 corners
def getCorners(theta, W, L, D, origin):

    listOfPoints = []

    x = origin[0]
    y = origin[1]

    baseForRightVerticies = getDistToRightCorners(L, D)
    perpForTopVerticies = getPerpForTopCorners(W)
    baseForLeftVertices = getDistToLeftCorners(L, D)
    perpForBottomVerticies = getPerpForBottomBottomCorners(W)

    x_tTopRight = x + baseForRightVerticies
    y_tTopRight = y + perpForTopVerticies
    # returns a list of length 2
    topRight = findNewCorner(theta, x_tTopRight, y_tTopRight)

    x_tBottomRight = x + baseForRightVerticies
    y_tBottomRight = y + perpForBottomVerticies
    bottomRight = findNewCorner(theta, x_tBottomRight, y_tBottomRight)

    x_tTopLeft = x + baseForLeftVertices
    y_tTopLeft = y + perpForTopVerticies
    topLeft = findNewCorner(theta, x_tTopLeft, y_tTopLeft)

    x_tBottomLeft = x + baseForLeftVertices
    y_tBottomLeft = y + perpForBottomVerticies
    bottomLeft = findNewCorner(theta, x_tBottomLeft, y_tBottomLeft)

    listOfPoints.append(topRight)
    listOfPoints.append(bottomRight)
    listOfPoints.append(topLeft)
    listOfPoints.append(bottomLeft)

    return listOfPoints

# will return a list of size two
def findNewCorner(theta, x_t, y_t):

    translationMatrix = buildTranslationMatrix(theta, x_t, y_t)
    coordMatrix = buildCoordMatrix(theta, x_t, y_t)

    answerMatrix = np.dot(translationMatrix, coordMatrix)

    answer = [answerMatrix[0], answerMatrix[1]]
    return answer


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

def getNextJoint(theta, W, L, D, origin):

    # get x and y
    x = origin[0]
    y = origin[1]

    # get the translation
    x_t = origin[0] + W
    y_t = origin[1] + 0

    translationMatrix = buildTranslationMatrix(theta, x_t, y_t)
    coordMatrix = buildCoordMatrix(x, y)

    answerMatrix = np.dot(translationMatrix, coordMatrix)

    # convert our answer to a list
    list = [answerMatrix[0], answerMatrix[1]]
    return list


def buildTranslationMatrix(theta, x_t, y_t):

    matrix = ([math.cos(theta), -(math.sin(theta)), x_t],
              [math.sin(theta), math.cos(theta), y_t],
              [0, 0, 1])

    return matrix

def buildCoordMatrix(x, y):

    matrix = ([x, y, y])
    return matrix


if __name__ == "__main__":
    chain = get_chain_msg()
    plot_chain(chain.config, chain.W, chain.L, chain.D)