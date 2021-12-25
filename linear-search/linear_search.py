def linear_search(lst, to_find):
  # search for the element to_find inside lst
  # if found, return index of element
  # else return -1
  # for i in range(len(lst)):
    # if lst[i] == to_find:
    #     return i
  if to_find < len(lst):
    return lst[to_find]
  return -1
    

# print(linear_search([1, 2, 3, 4], 1))
