def threeSum(self, nums: List[int]) -> List[List[int]]:
    #sort array first
    nums.sort()
    n = len(nums)
    res = []

    for i in range(n):
        if nums[i] > 0:
            break
        elif i > 0 and nums[i] == nums[i - 1]:
            continue
        #use two pointer to navigate from left and right in list
        lo, hi = i + 1, n - 1
        while lo < hi:
            total = nums[i] + nums[lo] + nums[hi]
            if total == 0:
                res.append([nums[i], nums[lo], nums[hi]])
                lo, hi = lo + 1, hi - 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
                while lo < hi and nums[hi] == nums[hi + 1]:
                    hi -= 1
            elif total < 0:
                lo = lo + 1
            else:
                hi = hi - 1
    return res

