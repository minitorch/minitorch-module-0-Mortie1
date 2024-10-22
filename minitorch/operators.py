"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.


# Mathematical functions:
# - mul
def mul(a: float, b: float) -> float:
    return a * b


# - id
def id(a: float) -> float:
    return a


# - add
def add(a: float, b: float) -> float:
    return a + b


# - neg
def neg(a: float) -> float:
    return -a


# - lt
def lt(a: float, b: float) -> bool:
    return a < b


# - eq
def eq(a: float, b: float) -> bool:
    return a == b


# - max
def max(a: float, b: float) -> float:
    return a if lt(b, a) else b


# - is_close
def is_close(a: float, b: float) -> bool:
    return abs(a - b) < 1e-2


# - sigmoid
def sigmoid(a: float) -> float:
    if a >= 0:
        return 1.0 / (1.0 + math.exp(-a))
    return math.exp(a) / (1 + math.exp(a))


# - relu
def relu(a: float) -> float:
    return max(0, a)


# - log
def log(a: float) -> float:
    return math.log(a)


# - exp
def exp(a: float) -> float:
    return math.exp(a)


# - log_back
def log_back(a: float, n: float) -> float:
    return (1 / a) * n


# - inv
def inv(a: float) -> float:
    return 1 / a


# - inv_back
def inv_back(a: float, n: float) -> float:
    return -1 / (a * a) * n


# - relu_back
def relu_back(a: float, n: float) -> float:
    return 1 * n if a > 0 else 0


#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


def map(f: Callable, a: Iterable) -> Iterable:
    for i in a:
        yield f(i)


def zipWith(a: Iterable, b: Iterable) -> Iterable:
    a, b = iter(a), iter(b)
    while True:
        try:
            yield (next(a), next(b))
        except StopIteration:
            return


def reduce(f: Callable[[float, float], float], a: Iterable) -> float:
    start = True
    res = 0.0
    for i in a:
        if start:
            res = i
            start = False
        else:
            res = f(res, i)
    return res


def negList(a: list) -> list:
    return list(map(neg, a))


def addLists(a: list, b: list) -> list:
    return list(map(lambda x: reduce(add, x), zipWith(a, b)))


def sum(a: list) -> float:
    return reduce(add, a)


def prod(a: list) -> float:
    return reduce(mul, a)
