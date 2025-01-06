class Solution:
    def bubble_sort(self, arr):
        for i in range(len(arr)):
            for j in range(0, len(arr)-i-1, 1):
                if (arr[j+1] < arr[j]):
                    arr[j+1], arr[j] = arr[j], arr[j+1]
        return arr


    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        sorted = self.bubble_sort(nums1)
        n = len(nums1)
        if (len(sorted) % 2 == 0):
            m = int(n/2)
            median = (sorted[m - 1] + sorted[m])/ 2
        else:
            median = sorted[int(n / 2)]
        print(median)

Obj = Solution()
Obj.findMedianSortedArrays([1,3], [2,5])