from collections import Counter



def sock_merchant0(n, ar):
    """
    Returns an integer representing the number
    of matching pairs of socks that are available.
    @param n: The number of socks in a pile
    @param ar: The colors of each sock
    return: An integer representing the number of
            matching pairs of socks that are available.
    rtype: int
    """
    # . THINK: You're given n for a reason -- use it?
    #      - Hmm, including n may have actually been an
    #        error while translating this problem from
    #        other programming languages...

    # NOTE: There's a class in collections called Counter
    #       that can construct the result of the following
    #       loop all in one line! ==> Counter(ar)
    # . Keep a scoreboard of sock counts
    result = {}
    for e in ar:
        if e not in result:
            result[e] = 1
        else:
            result[e] += 1

    return sum([e//2 for e in result.values()])


def sock_merchant1(n, ar):
    """
    A one-liner solution
    """
    return sum([e//2 for e in Counter(ar).values()])



solution = sock_merchant1
if __name__ == "__main__":
    n = 9
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

    # Target output: 3 ([20,20], [10,10], [10,10])

    result = solution(n, ar)
    print(result)
