#   The goal of this question is to write a software library that accepts 2 version string as input
#   and returns whether one is greater than, equal, or less than the other.
#   As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.

#   Assume that the version format is of the form V = X.Y.Z (Major.Minor.Patch)
#   String v1 and string v2
#   Return 1 if v1 > string v2
#   Return 0 if v1 == v2
#   Return -1 if v1 < v2

def compare(v1, v2):
    a = v1.split(".")       #   This splits it into string elements eg 1.2.3 to 3 and 1.2 to 2 elements
    b = v2.split(".")

    #   Maximum length needed for comparison
    m = min (len(a), len(b))

    # If a list is smaller than the other, just add a 0 at the end to make them equal length for comparison
    for i in range(0, m - 1):
        if len(a) < max(len(a), len(b)):
            a.append('0')
        elif len(b) < max(len(a), len(b)):
            b.append('0')

    #   Comparing elements of the 2 list to find which is an updated version of the other.
    for i in range(0, m):     #
        if a[i] < b[i]:
            return -1
        elif a[i] > b[i]:
            return 1
    return 0
