class Solution:
    def isPalindrome(self, x):
        con_str = str(x)
        rev_str = con_str[::-1]
        print(con_str)
        print(rev_str)
        if (con_str == rev_str):
            return True
        else:
            return False
        
obj = Solution()
print(obj.isPalindrome(-121))
        