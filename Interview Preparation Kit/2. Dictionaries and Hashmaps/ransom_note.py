from collections import Counter


def check_magazine0(magazine, note):
    """
    Determines if some note can be constructed from
    a list of words repersenting a magazine article.
    "Yes" is printed if the construction is possible
    or "No" otherwise
    @param magazine: A list of strings representing a
                     magazine article that we can get
                     words from
    @param note: A list of strings representing some
                 target ransom note we'd like to produce
    return: None
    rtype: None
    """
    # Basic problem:
    # Given two dictionaries, tell if one of them
    # is a subset of the other

    # THINK:
    # - What if there's a case where note has two words of
    #   something while magazine only has one instance of that
    #   word? Using sets would generate only one unique instance
    #   of all words...and it would produce the wrong result
    #   in this case...

    # . Make a dict of word counts for magazine and note
    # . Iterate through the keys of note. If the corresponding keys in
    #   magazine has the same count as in note, then "YES". However,
    #   if there's just a single mismatch in counts, then "NO".
    mag_d = Counter(magazine)
    note_d = Counter(note)
    for k in note_d:
        if mag_d[k] < note_d[k]:
            print("No")
            return

    print("Yes")


def check_magazine1(magazine, note):
    """
    Using ternary operator
    """
    mag_d = Counter(magazine)
    note_d = Counter(note)
    print("Yes") if all([mag_d[k] >= note_d[k] for k in note_d]) else print("No")




solution = check_magazine1
if __name__ == "__main__":
    magazine = "two times three is not four".split(" ")
    note = "two times two is four".split(" ")

    solution(magazine, note)
