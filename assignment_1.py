# Assignment 1 Tempate
#
# Author's Name: Pek Tze Hng, Zachary
# Author's ID: A0322774B
#

# Task 1: absolute difference between two roots
# =============================================

from math import sqrt

def rootsCharacter(a, b, c):
    # Calculates and characterises the roots of a quadratic equation of the form ax^2 + bx + c = 0, where b^2 >= 4ac.
    #
    # Args:
    #     a (float): coefficient of x^2 term of quadratic equation.
    #     b (float): coefficient of x term of quadratic equation.
    #     c (float): constant term of quadratic equation.
    #
    # Returns:
    #     int:
    #        1 if both roots are positive,
    #        -1 if both roots are negative, 
    #        0 otherwise.

    discriminant = b ** 2 - 4 * a * c # non-negative as b^2 >= 4ac and hence b^2 - 4ac >= 0
    sqrt_discriminant = sqrt(discriminant) # compute once and store in sqrt_discriminant, will not raise ValueError as discriminant is non-negative
    denominator = 2 * a # compute once and store in denominator
    root_1 = (-b + sqrt_discriminant) / denominator
    root_2 = (-b - sqrt_discriminant) / denominator
    root_1_positive = root_1 > 0 # computes a boolean (True if root_1 is positive and False if root_1 is negative) once and stores in root_1_positive
    root_2_positive = root_2 > 0 # computes a boolean (True if root_2 is positive and False if root_2 is negative) once and stores in root_2_positive
    return 1 if root_1_positive and root_2_positive \
        else -1 if not root_1_positive and not root_2_positive \
            else 0


# Task 2: polygon area
# ====================

from math import *

def perimeterPoly(n, d):
    return n * d

def apothemPoly(n, d):
    return d / (2 * tan(pi / n))

def areaPoly(n, d):
    # Calculates the area of a regular polygon.
    # 
    # Args:
    #     n (int): number of corners in the polygon.
    #     d (float): length of one of the sides of the polygon.
    # 
    # Returns:
    #     float: area of the polygon.

    perimeter = n * d
    apothem = d / (2 * tan(pi / n))
    area = perimeter * apothem / 2
    return area

def polySide(n, area):
    # Calculates the length of one of the sides of a regular polygon.
    # 
    # Args:
    #     n (int): number of corners in the polygon.
    #     area (float): area of the polygon.
    #
    # Returns:
    #     float: length of one of the sides of the polygon. 

    return sqrt((4 * area * tan(pi / n)) / n)


# Task 3: Area of a circle with an inscribed square
# =================================================

from math import pi

def find_circumcircle_area(sq_side):
    # Insert code and comments below
    pass # delete this line before submitting your code


# Task 4: Gradient of a function at a point
# =========================================

def derivative(f):
    # Insert code and comments below
    pass # delete this line before submitting your code