import cv2
from math import sqrt, atan2, sin, cos
import numpy as np
import random


def lightning(img, pt1, pt2):

    width = 30  # Bandwidth of nodes

    # generate a list of nodes in a certain area in order from left to right according to slope to connect later

    degree = atan2(-(pt2[0]-pt1[0]), (pt2[1]-pt1[1]))

    nodes = []  # List of points
    nodes_length = 10

    x = np.linspace(pt2[0], pt1[0], nodes_length)
    y = np.linspace(pt2[1], pt1[1], nodes_length)
    for i in range(nodes_length):

        pt = np.array([x[i], y[i]])

        if i == 0 or i == nodes_length-1:
            nodes.append((int(pt[0]), int(pt[1])))  # add node into the list
            continue

        random_displacement = ((random.random()*2)-1)*width
        pt[0] += cos(degree)*random_displacement
        pt[1] += sin(degree)*random_displacement

        nodes.append((int(pt[0]), int(pt[1])))  # add node into the list

    for i in range(nodes_length-1):
        cv2.line(img, nodes[i], nodes[i+1], (208, 224, 64), 3)
