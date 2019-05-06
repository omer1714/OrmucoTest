#   Your goal for this question is to write a program that accepts
#   two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap.
#   As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).

#   Assumptions
#   a <= b and a < c
#   c <= d and b < d

def isOverlapping (a, b, c, d):
    if a==b & b==c:
        return True
    elif a < c & b >= c:
        return True
    elif a >= c & a <= d:
        return True
    elif a < c & b >= c:
        return True
    elif a >= c & a >= d:
        return False
    elif a < c & b < c:
        return False
