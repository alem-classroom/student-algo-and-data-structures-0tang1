def binary_search(lst, to_find):
    # search for the element to_find inside lst
    # if found, return index of element
    # else return -1
    l = 0
    r = len(lst)-1
    while l <= r:
        m = (l+r) // 2
        if lst[m] == to_find:
            return m
        elif to_find < lst[m]:
            r = m-1
        elif to_find > lst[m]:
            l = m+1
    return -1

# print(binary_search([1,2,3,4,5], 2))
