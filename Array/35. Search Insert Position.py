def searchInsert(self, nums: List[int], target: int) -> int:
    for i, v in enumerate(nums):
        if v == target:
            return i
    return bisect_left(nums, target)