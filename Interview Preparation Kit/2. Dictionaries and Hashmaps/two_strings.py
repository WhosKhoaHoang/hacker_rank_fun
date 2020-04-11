


def two_strings(s1, s2):
    """
    Prints "YES" if s1 and s2 share a common substring
    or "NO" otherwise.
    @param s1: The first string to check
    @param s2: The second string to check
    return: None
    rtype: None
    """
    # Since we're only looking for a simple "YES" or "NO"
    # with regards to whether or not any substring is
    # common at all, it is sufficient to just check if
    # there is any intersection between the components
    # of the strings (i.e., the string's characters).
    # We can convert the strings to sets of characters
    # and use the & operator to check for the common
    # elements.
    return "YES" if set(s1) & set(s2) else "NO"




if __name__ == "__main__":
    s1 = "be"
    s2 = "cat"
    s1 = "hello"
    s2 = "world"
    result = two_strings(s1, s2)
    print(result)
