class Solution:
    def maxArea_beyondtime(self, height):
        max_area = 0
        len_arr = len(height)
        for i in range(0,len_arr, 1):
            for j in range(i+1,len_arr, 1):
                if(max_area <= (min(height[i], height[j]) * (j-i))):
                    max_area = (min(height[i], height[j]) * (j-i))
        return max_area
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        res = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            res = max(res, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res
obj = Solution()
print(obj.maxArea([1,2,6,1]))
print(obj.maxArea([1,8,6,2,5,4,8,3,7]))




        