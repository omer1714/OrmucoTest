#   Your goal for this question is to write a program that accepts
#   two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap.
#   As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).

#   Assumptions
#   x1 <= x2 and x1 < x3
#   x3 <= x4 and x2 < x4

def isOverlapping (a, b, c, d):
    if a == b & b != c:
        return False        #   First line is a point and the end point of one doesnt overlap the starting point of the other line
    elif a <= c & b < c:
        return False        #   They do not overlap a is assumed to be always less than c
    elif a < c & b >= c:
        return True         #   Result overlaps at C
    elif a >= c & a <= d:
        return True         #   If a is between c and d that means it overlaps
    elif a == c & b < d:
        return True         #   If a and c are the same starting point but b is less than d then they overlap
    elif a == c & b > d:
        return True         #   If a and c are the same starting point but b is greater than d then they overlap
    elif a >= c & a >= d:
        return False