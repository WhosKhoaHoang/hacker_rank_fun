


def left_rotation0(lst, d):
    """
    @param lst: The list to rotate left by d
    @param d: The number of times to rotate left
    return: A list containing elements of the original
            lst with their positions rotated left d times
    rtype: list
    """
    # THINK: Any way we can do this in-place?
    result = [0]*len(lst)
    for i in range(len(lst)):
        result[i-d] = lst[i]

    return result



solution = left_rotation0
if __name__ == '__main__':
    a = [1,2,3,4,5]
    d = 4
    # Target output: [5, 1, 2, 3, 4]

    # . For each element, consider its index
    # . Since it's a movement towards the left, think of substraction
    # . Subtract the index by d
    #    - E.g., if d = 1 and an element is at idx = 1,
    #      then idx - d = 0. The element's index is changed to 0.

    # APPROACH:
    # - Create a list of 0s whose length is the same as lst
    # - Iterate through list using for i in range.
    # - Take the index and the element, subtract the index by d, and
    #   set it to the (idx-d)'th position of the 0-list

    result = solution(a, d)
    print(" ".join(map(str, result)))
