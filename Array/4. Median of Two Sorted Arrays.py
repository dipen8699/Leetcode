def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #sum of two array
    merged_array = nums1 + nums2
    #sort array
    merged_array.sort()
    mid = len(merged_array) // 2
    #apply Binary search and Divide&Conquer
    if len(merged_array) % 2 == 0:
        return (merged_array[mid - 1] + merged_array[mid]) / 2
    else:
        return merged_array[mid]