class Solution:
    def longestPalindrome(self, s):
        res = ''
        for i in range(len(s)):
            for j in range(i+1, len(s)+1, 1):
                temp = s[i:j]
                if (temp == temp[::-1] and len(temp) > len(res)):
                    res = temp
        return res
    
obj = Solution()
obj.longestPalindrome('badad')