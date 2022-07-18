def twoSum(nums,target):
	twosum = {}
	for i,val in enumerate(nums):
		if target - val in twosum:
			return [twosum[target-val],i]
		twosum[val] = i
	return []





if __name__ == '__main__':
	test1 = [1,2,5,7,8]
	target1 = 7

	test2 = [11,23,45,12,2,3]
	target2 = 48


	ans1 = twoSum(test1,target1)
	print(ans1)

	ans2 = twoSum(test2,target2)
	print(ans2)
