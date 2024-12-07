def minimumSize(self, nums: List[int], maxOperations: int) -> int:
    def can_divide(m):
        ops = 0
        for n in nums:
            ops += ceil(n / m) - 1
            if ops > maxOperations:
                return False
        return True

    low, high = 1, max(nums)
    res = high

    while low < high:
        mid = low + (high - low) // 2
        if can_divide(mid):
            high = mid
            res = high
        else:
            low = mid + 1
    return res