# Mid-week challenge
# Name: Christopher Van Schyndel

import math


# This function will find the area of a rectangle, triangle, or circle, based
# on the corresponding arguments explicitly given.
# For a triangle, give the base and height, or the measurement
# of the three sides- side1, side2, and side3.
# For a circle, give the radius.
# For a rectangle, give the height and width.
# Ex: find_area(base=5, height=5) returns the area of a triangle.
def find_area(base=0, height=0, side1=0, side2=0, side3=0, radius=0, width=0):
    # For calculating triangle area, if base + height are given
    if base > 0 and height > 0:
        area = 0.5 * ( base * height )
    # For calculating triangle area, if all three sides are given
    if side1 > 0 and side2 > 0 and side3 > 0:
        # Calculate semiperimeter
        sp = (side1 + side2 + side3) / 2.0
        area = math.sqrt(sp * ( sp - side1 ) * ( sp - side2 ) * ( sp - side3 ))
    # For calculating circle area, if radius is given
    if radius > 0:
        area = math.pi * (radius ** 2)
    # For calculating rectangle area, if width and height are given
    if width > 0 and height > 0:
        area = width * height
    return area
