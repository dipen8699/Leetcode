def threeSumClosest(self, nums: List[int], target: int) -> int:
    nums.sort()
    n = len(nums)
    res = float('inf')

    for i in range(n):

        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # same approach like 3 sum with some modification
        lo, hi = i + 1, n - 1
        while lo < hi:
            total = nums[i] + nums[lo] + nums[hi]
            if abs(total - target) < abs(res - target):
                res = total
            elif total < target:
                lo += 1
            elif total > target:
                hi -= 1
            else:
                return total
    return res