def selection_sort(lst):
    # sort the list via selection sort
    if len(lst) == 1:
        return lst
    else:
        for i in range(len(lst)):
            min_el = i

            for j in range(i+1, len(lst)):
                if lst[min_el] > lst[j]:
                    min_el = j
            
            lst[min_el], lst[i] = lst[i], lst[min_el]
    return lst

# a = selection_sort([1,5,2,7,8,3,0])
# print(a)
