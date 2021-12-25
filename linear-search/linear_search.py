def linear_search(lst, to_find):
  # search for the element to_find inside lst
  # if found, return index of element
  # else return -1
  for el in lst:
    if el == to_find:
        return lst.index(el)
    else:
        return -1

# print(linear_search([1, 2, 3, 4], 1))
