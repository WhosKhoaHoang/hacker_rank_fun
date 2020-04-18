


def kangaroo(x1, v1, x2, v2):
    """
    Determines if two kangaroos can eventually (?) end up
    in the same position after jumping from some starting
    position (after some number of jumps?).
    @param x1: The start position of the 1st kangaroo
    @param v1: The jump rate of the 1st kangaroo (meters/jump)
    @param x2: The start distance of the 2nd kangaroo
    @param v2: The jump rate of the 2nd kangaroo (meters/jump)
    return: True if the two kangaroos end up at the
            same position or false otherwise
    rtype: boolean
    """
    # The problem statement's constraints note that
    # the starting position for kangaroo 1 is less
    # than kangaroo 2's. I.e.,
    #    0 <= x1 < x2 <= 10000

    # . v1 and v2 are rates of change (slope in 2D plane)
    # . x1 and x2 are initial positions (y-intercept in 2D plane)
    # Consider:
    #     x1 + j*v1 = x2 + j*v2
    # where j is the number of jumps. If we solve for j,
    # we get j = (x1-x2)/(v2-v1). Assuming that it
    # only makes sense for j to be a whole number, the
    # two kangaroos will eventually meet if (v2-v1)
    # divides evenly into (x1-x2). I.e., if:
    #      (x1-x2) % (v1-v2) == 0

    # If v1 is greater than v2, then kangaroo 1
    # has a chance of landing in the same position
    # as kangaroo 2 somewhere down the line.
    if v1 > v2:
        if (x1-x2) % (v1-v2) == 0:
            return True
    return False



if __name__ == "__main__":
    x1, v1, x2, v2 = 0, 2, 5, 3
    x1, v1, x2, v2 = 0, 2, 5, 3

    result = kangaroo(x1, v1, x2, v2)
    print(result)
