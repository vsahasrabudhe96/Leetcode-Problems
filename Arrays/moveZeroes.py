def moveZeroes(nums):
    """_summary_

    Args:
        nums (List): List of zeroes
    """
    ## Brute Force
    res = []
    k = nums.count(0)
    if k == 0:
        return nums
    else:
        for i in nums:
            if i!=0:
                res.append(i)
        for i in range(k):
            res.append(0)
        return res
    
    
    ## In O(1) space
    
    
if __name__ == '__main__':
    t1 = [0,1,0,3,12]
    t2 = [0,0,0,0,0,1]
    a1 = moveZeroes(t1)
    print(a1)
    
    a2 = moveZeroes(t2)
    print(a2)
    assert(a1 == [1,3,12,0,0])
    assert(a2 == [1,0,0,0,0,0])
    
    