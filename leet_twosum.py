# solving two sum using hashmap for better time & memory complexity
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for indx,val in enumerate(nums):
            diff = target -val
            if (diff) in d:
                return [d[diff], indx]
            d[val] = indx
        print(nums)
        print(target)
    
obj = Solution()
print(obj.twoSum([2,7,11,15], 9))
print(obj.twoSum([3,2,4], 6))

# loop1 : d= {2: 0}
# loop2 : d=