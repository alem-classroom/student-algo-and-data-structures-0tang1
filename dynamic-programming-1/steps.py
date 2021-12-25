def steps(num):
    # solve the problem via dynamic programming
    # return number of required steps
    f0 = 0
    f1 = 1
    if num <= 2 and num >= 0:
    	return num
    elif num == 3:
        return 2
    else:
    	for i in range(num):
    		fn = f0 + f1
    		f0 = f1
    		f1 = fn
    	return f1
    

# print(steps(7))
