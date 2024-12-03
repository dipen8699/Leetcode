def containsDuplicate(self, nums: List[int]) -> bool:
    # create hashtable and sort array
    hashset = set()

    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)
    return False