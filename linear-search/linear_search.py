def linear_search(lst, to_find):
  # search for the element to_find inside lst
  # if found, return index of element
  # else return -1
  res = -1
  for i in range(len(lst)):
    if lst[i] == to_find:
        res  = i
  return res
    

# print(linear_search([1, 2, 3, 4], 1))
