def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
    nums.sort()
    ans = 0

    for i, v in enumerate(nums):
        l_b = bisect_left(nums, lower - v, i + 1)
        u_b = bisect_right(nums, upper - v, i + 1)
        ans += (u_b - l_b)
    return ans