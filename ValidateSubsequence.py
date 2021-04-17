def isValidSubsequence(array, sequence):
    # Write your code here.
    p1 = 0
	p2 = 0
	
	while p1 < len(array) and p2 < len(sequence):
		if array[p1] == sequence[p2]:
			p1 += 1
			p2 += 1
		else:
			p1 += 1
	
	return p2 == len(sequence)

