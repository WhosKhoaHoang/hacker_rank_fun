


def counting_valleys0(s):
    """
    Determines the number of valleys that were
    walked through given a sequence of characters
    representing an altitudinal traveral ("U" stands
    for "up", "D" stands for "down").
    Important definitions:

    . A mountain is a sequence of consecutive
      steps **above sea level**, starting with a
      step up from sea level and ending with a
      step down to sea level.
    . A valley is a sequence of consecutive steps
      **below sea level**, starting with a step down
      from sea level and ending with a step up to
      sea level.

    @param s: The sequence of alitudinal traversals (e.g.,
              "UDDDUDUU")
    type s: str
    return: The number of valleys walked through
    rtype: int
    """
    # . Let v_steps track consecutiveness
    # . If positive to negative and if v_steps < 2, then
    #   increment v_steps
    # . If negative to positive, then reset v_steps to 1
    #   and increment valleys
    # . THINK: You can easily implement a mountains passed
    #          counter if you switch inequalities
    prev_sl, cur_sl = 0, 0
    v_steps, valleys = 0, 0
    m_steps, mountains = 0, 0  # For fun
    for c in s:
        prev_sl = cur_sl
        if c == "U": cur_sl += 1
        elif c == "D": cur_sl -= 1

        # For mountains (for fun)
        if prev_sl <= 0 and cur_sl > 0 and m_steps < 2:
            m_steps += 1
        elif prev_sl > 0 and cur_sl <= 0:
            m_steps = 0
            mountains += 1

        # For valleys
        if prev_sl >= 0 and cur_sl < 0 and v_steps < 2:
            v_steps += 1
        elif prev_sl < 0 and cur_sl >= 0:
            v_steps = 0
            valleys += 1

    #return (valleys, mountains)
    return valleys



solution = counting_valleys0
if __name__ == "__main__":
    s = "UDDDUDUU"

    # Target output: 1
    # If we represent _ as sea level, a step up as /,
    # and a step down as \, Gary's hike can be drawn as:
    # _/\      _
    #    \    /
    #     \/\/

    result = solution(s)
    print(result)
