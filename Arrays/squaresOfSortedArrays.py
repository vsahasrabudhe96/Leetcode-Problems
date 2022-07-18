def squaresOfSortedArrays(nums):
	'''
		input: List of Integers
		output: List of Integers

		Description of Function:
		Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

		Example 1:

		Input: nums = [-4,-1,0,3,10]
		Output: [0,1,9,16,100]
		Explanation: After squaring, the array becomes [16,1,0,9,100].
		After sorting, it becomes [0,1,9,16,100].
	'''
	# Brute Force
	return sorted([c**2 for c in nums])

	#Optimal Solution using 2 pointers
	




if __name__ == '__main__':

	t_1 = [-4,-1,0,3,10]
	t_2 = [-7,-3,2,3,11]

	a1 = squaresOfSortedArrays(t_1)
	a2 = squaresOfSortedArrays(t_2)
	print(a1)
	print(a2)

