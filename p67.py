
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # lst = list(set(nums))
    # uniques = len(lst)
    # for e in lst:
    #     if nums.count(e)>1:
    #         for i in range(1,nums.count(e)):
    #             lst.append("_")
    # return uniques, lst
    nums = list(set(nums))
    k = len(nums)
        
    return nums

print(removeDuplicates([1,1,2]))