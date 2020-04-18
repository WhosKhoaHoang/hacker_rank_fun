
# NOTE:
# . Sam's house lies on some interval [s, t]
# . An apple tree lies at point a
# . An orange tree lies at point b
# . m apples will drop some number of units from a
# . n oranges will drop some number of units from b


def countApplesAndOranges(s, t, a, b, apples, oranges):
    """
    Returns the number of apples and oranges that fall
    within range of Sam's house.
    @param s: Left inclusive endpoint of Sam's house
    @param t: Right inclusive endpoint of Sam's house
    @param a: The location of the apple tree
    @param b: The location of the orange tree
    @param apples: The number of units the apples dropped from a
    @param oranges: The number of units the oranges dropped from b
    type s: int
    type t: int
    type a: int
    type b: int
    type apples: [int]
    type apples: [int]
    return: The number of apples and oranges that fall
            within range of Sam's house.
    rtype: list
    """
    result = [0, 0]
    sams_house = range(s, t+1)
    for apple in apples:
        if (a+apple) in sams_house:
            result[0] += 1
    for orange in oranges:
        if (b+orange) in sams_house:
            result[1] += 1

    return result


if __name__ == "__main__":
    s, t = 7, 11
    a, b = 5, 15
    apples = [-2, 2, 1]
    oranges = [5, -6]

    result = countApplesAndOranges(s, t, a, b, apples, oranges)
    print(result[0])
    print(result[1])
