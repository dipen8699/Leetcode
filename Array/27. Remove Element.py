def removeElement(self, nums: List[int], val: int) -> int:
    j = 0
    #same approach as remove duplicate from array
    for i in range(0, len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
    return j