import math
import random
from dataclasses import dataclass
from typing import List, Tuple


def make_pts(N: int) -> List[Tuple[float, float]]:
    """Generate a list of random 2D points.

    This function creates a list of `N` tuples, each representing a point
    in 2D space with random x and y coordinates between 0 and 1.

    Args:
    ----
        N (int): The number of points to generate.

    Returns:
    -------
        List[Tuple[float, float]]: A list of tuples where each tuple contains
        two float values representing the x and y coordinates of a point.

    """
    X = []
    for i in range(N):
        x_1 = random.random()
        x_2 = random.random()
        X.append((x_1, x_2))
    return X


@dataclass
class Graph:
    N: int
    X: List[Tuple[float, float]]
    y: List[int]


def simple(N: int) -> Graph:
    """Generate a simple dataset with a binary label based on x-coordinate.

    This function generates a dataset of N random 2D points and assigns a binary label
    to each point based on the x-coordinate. The label is 1 if the x-coordinate is less
    than 0.5, otherwise it is 0.

    Args:
    ----
        N (int): The number of data points to generate.

    Returns:
    -------
        Graph: A Graph object containing the generated points and their labels.

    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def diag(N: int) -> Graph:
    """Generate a dataset with a binary label based on the sum of the x and y coordinates.

    This function generates a dataset of N random 2D points and assigns a binary label
    to each point based on the sum of the x and y coordinates. The label is 1 if the sum is less
    than 0.5, otherwise it is 0.

    Args:
    ----
        N (int): The number of data points to generate.

    Returns:
    -------
        Graph: A Graph object containing the generated points and their labels.

    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 + x_2 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def split(N: int) -> Graph:
    """Generate a dataset with a binary label based on the x-coordinate. The label is 1 if the x-coordinate is less than 0.2 or greater than 0.8, otherwise it is 0.

    Args:
    ----
        N (int): The number of data points to generate.

    Returns:
    -------
        Graph: A Graph object containing the generated points and their labels.

    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.2 or x_1 > 0.8 else 0
        y.append(y1)
    return Graph(N, X, y)


def xor(N: int) -> Graph:
    """Generate a dataset with a binary label based on the XOR condition of x and y coordinates.

    This function generates a dataset of N random 2D points and assigns a binary label
    to each point based on the XOR condition of its coordinates. The label is 1 if either
    the x-coordinate is less than 0.5 and the y-coordinate is greater than 0.5, or the
    x-coordinate is greater than 0.5 and the y-coordinate is less than 0.5; otherwise, it is 0.

    Args:
    ----
        N (int): The number of data points to generate.

    Returns:
    -------
        Graph: A Graph object containing the generated points and their labels.

    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.5 and x_2 > 0.5 or x_1 > 0.5 and x_2 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def circle(N: int) -> Graph:
    """Generate a dataset with a binary label based on whether a point is inside a circle or not.

    This function generates a dataset of N random 2D points and assigns a binary label
    to each point based on whether it is inside a circle with a center at (0.5, 0.5) and a radius of 0.31622776601683794. The label is 1 if the point is inside the circle and 0 if it is outside the circle.

    Args:
    ----
        N (int): The number of data points to generate.

    Returns:
    -------
        Graph: A Graph object containing the generated points and their labels.

    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        x1, x2 = x_1 - 0.5, x_2 - 0.5
        y1 = 1 if x1 * x1 + x2 * x2 > 0.1 else 0
        y.append(y1)
    return Graph(N, X, y)


def spiral(N: int) -> Graph:
    """Generate a dataset with a binary label based on the spiral dataset.

    This function generates a dataset of N points in a spiral shape. The first N/2 points have a label of 0 and the second N/2 have a label of 1.

    Args:
    ----
        N (int): The number of data points to generate.

    Returns:
    -------
        Graph: A Graph object containing the generated points and their labels.

    """

    def x(t: float) -> float:
        return t * math.cos(t) / 20.0

    def y(t: float) -> float:
        return t * math.sin(t) / 20.0

    X = [
        (x(10.0 * (float(i) / (N // 2))) + 0.5, y(10.0 * (float(i) / (N // 2))) + 0.5)
        for i in range(5 + 0, 5 + N // 2)
    ]
    X = X + [
        (y(-10.0 * (float(i) / (N // 2))) + 0.5, x(-10.0 * (float(i) / (N // 2))) + 0.5)
        for i in range(5 + 0, 5 + N // 2)
    ]
    y2 = [0] * (N // 2) + [1] * (N // 2)
    return Graph(N, X, y2)


datasets = {
    "Simple": simple,
    "Diag": diag,
    "Split": split,
    "Xor": xor,
    "Circle": circle,
    "Spiral": spiral,
}
