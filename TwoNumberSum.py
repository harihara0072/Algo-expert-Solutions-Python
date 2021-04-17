def twoNumberSum(array, targetSum):
    # Write your code here.
    util = {}
	for num in array:
		if num in util:
			return [num, targetSum - num]
		
		util[targetSum - num] = True
	
	return []


