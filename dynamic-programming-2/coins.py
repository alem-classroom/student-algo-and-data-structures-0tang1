def maxCoins(lst, n):
    # return maximum number of coins that can be acquired in the maze
    for i in range(1, n):
        lst[0][i] += lst[0][i-1]
        lst[i][0] += lst[i-1][0]
    
    for i in range(1, n):
        for j in range(1, n):
            if lst[i-1][j] < lst[i][j-1]:
                lst[i][j] += lst[i][j-1]
            else:
                lst[i][j] += lst[i-1][j]
    
    return lst[n-1][n-1]


# lst = [[3, 1, 4, 9, 9], [2, 4, 9, 6, 8], [7, 4, 9, 1, 7], [1, 2, 1, 2, 2], [2, 4, 9, 5, 5]]
# n = 5

# print(maxCoins(lst, n))
