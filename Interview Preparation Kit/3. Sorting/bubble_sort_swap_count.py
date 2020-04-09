


def bubble_sort_sc(a):
    """
    Prints the number of swaps needed for a bubble
    sort procedure on the given list a.
    @param a: The list of integers to bubble sort
              and count the swaps for.
    type a: list
    return: None
    rtype: None
    """
    swaps = 0
    for i in range(len(a)):
        for j in range(len(a)-1): #
        # Can also optimize by saying (len(a)-i-1) since the
        # last i elements are already sorted
            if a[j] > a[j+1]:
                swaps += 1
                a[j], a[j+1] = a[j+1], a[j]

    print(f"Array is sorted in {swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")

    return a




if __name__ == "__main__":
    lst = [3,2,1]
    bubble_sort_sc(lst)
