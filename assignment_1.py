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
    #     a (float or int): coefficient of x^2 term of quadratic equation.
    #     b (float or int): coefficient of x term of quadratic equation.
    #     c (float or int): constant term of quadratic equation.
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

def areaPoly(n, d):
    # Calculates the area of a regular polygon.
    # 
    # Args:
    #     n (int): number of corners in the polygon.
    #     d (float or int): length of one of the sides of the polygon.
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
    #     area (float or int): area of the polygon.
    #
    # Returns:
    #     float: length of one of the sides of the polygon. 
    
    polygon_side_length = sqrt((4 * area * tan(pi / n)) / n) # rearrange formula in areaPoly to make polygon side length d the subject
    return polygon_side_length


# Task 3: Area of a circle with an inscribed square
# =================================================

from math import pi

def find_circumcircle_area(sq_side):
    # Calculate the area of a circle in which a square is inscribed.
    #
    # Args:
    #    sq_side (float or int): length of a side of the square
    # 
    # Returns:
    #     float: area of the circle in which the square is inscribed 

    sq = lambda x: x * x
    diameter_squared = sq(sq_side) + sq(sq_side) # diameter of the circle is equal to the hypotenuse of the isosceles triangle with 2 of its sides as sq_side
    radius_squared = diameter_squared / sq(2)
    circumcircle_area = pi * radius_squared
    return circumcircle_area


# Task 4: Gradient of a function at a point
# =========================================

def derivative(f):
    # Derives a function which calculates the derivative or gradient at a point via the finite difference method
    #
    # Args:
    #     f (function): function to differentiate
    #
    # Returns:
    #     function: derivative of function f

    step_size = 1e-5
    derivative = lambda x: ((f(x + step_size) - f(x)) / step_size)
    return derivative