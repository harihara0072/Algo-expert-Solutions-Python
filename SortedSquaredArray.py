def sortedSquaredArray(array):
    # Write your code here.
    output = [None] * len(array)
	
	left = 0
	right = len(array) - 1
	i = len(array) - 1
	
	while left <= right:
		if abs(array[left]) <= abs(array[right]):
			output[i] = array[right] ** 2
			right -= 1
			
		else:
			output[i] = array[left] ** 2
			left += 1
			
		i -= 1
	
	return output
