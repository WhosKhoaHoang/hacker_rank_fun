


def jumping_on_clouds0(c):
    """
    Returns the minimum number of jumps required to
    navigate through a series of clouds represented by
    the provided list of integers with values {0, 1}
    (where 0 is a jumpable cloud and 1 is non-jumpable)
    @param c: A list of binary integers representing clouds
    type c: [int]
    return: The minimum number of jumps to reach the
            end of the clouds within the given constraints
    rtype: int
    """
    # Game rules:
    # . Some of the clouds are thunderheads and others are cumulus.
    # . Player can jump on any cumulus cloud having a number that is
    #   equal to the number (not the index, the NUMBER [i.e., 0]) of
    #   the current cloud plus 1 or 2.
    # . Player must avoid the thunderheads.
    # . Determine the minimum number of jumps it will take player to
    #   jump from her starting postion to the last cloud. It is always
    #   possible to win the game.

    # Approach:
    # . Always look ahead 2 steps. If the landing spot is on 1, then
    #   take the spot before it (the game shouldn't be able to have
    #   to 1s in a row because then that would make it impossible for
    #   the player to progress?)
    # . Add the path to a separate data structure?
    # . THINK: Access dict elements, not list elements
    # . Treat the the given c list as a queue and only append
    #   to path if it's a good pop? pop(0). Append indices?
    # . Length of a path is len(path)-1

    path = [0]  # Go the extra mile and provide path
    cur_idx = 0
    while cur_idx < len(c)-1:
        # Instead of peeking over to the next index if its 1,
        # how about we always try to hop over two spots instead?
        # It's killing two birds with one stone -- you hop the
        # hughest amount and you might hop over a 1 in the process!
        # Let the GREEDY nature of this algorithm guide you. With
        # that in mind, it could be sufficient to use only the
        # block of code (with some modification) inside this if statement.
        #  - Implementation of jumping_on_clouds1 takes this to heart
        if c[cur_idx+1] != 1:
            # If still within range...
            if (cur_idx+2) < len(c): # NOT len(c)-1
                if c[cur_idx+2] != 1:
                    cur_idx+=2
                else:
                    cur_idx+=1
            else:
                cur_idx+=1
        else:
            cur_idx+=2  # hop
        path.append(cur_idx)

    #print(path)
    return len(path)-1


def jumping_on_clouds1(c):
    """
    Optimized
    """
    #path = [0]
    result = 0
    cur_idx = 0
    while cur_idx < len(c)-1:
        if (cur_idx+2) < len(c) and c[cur_idx+2] != 1:
            cur_idx+=2
        else:
            cur_idx+=1

        #path.append(cur_idx)
        result += 1

    #print(path)
    #return len(path)-1
    return result




solution = jumping_on_clouds1
if __name__ == "__main__":
    #c = [0, 1, 0, 0, 0]
    #c = [0, 0, 1, 0]
    c = [0, 0, 1, 0, 0, 1, 0]  # Target: 4
    #c = [0, 1, 0, 0, 0, 1, 0]
    #c = list(map(int, input().rstrip().split()))

    # Target: 4
    # - Emma must avoid c[2] and c[5]. She can win
    #   the game with a minimum of 4 jumps
    #   (idxs: 0->1, 1->3, 3->4, 4->6)

    result = solution(c)
    print(result)
