def twoSum(nums: List[int], target: int) -> List[int]:
    #create empty hashset to store key-val pair
    prev_def = {}

    for i, n in enumerate(nums):
        deff = target - n
        if deff in prev_def:
            return [prev_def[deff], i]
        prev_def[n] = i
    return
