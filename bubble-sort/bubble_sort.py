def bubble_sort(lst):
    # sort the list via bubble sort
    sw = False
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[j] > lst[i]:
                lst[j], lst[i] = lst[i], lst[j]
                sw = True

        if sw == False:
            break
    
    return lst


# print(bubble_sort([1,5,2,3,4,8]))
