class Solution:
    def reverse(self, x):
        if x > 0:
            temp = str(x)[::-1]
            if (int(temp) <= ((2**31)-1)):
                return int(temp)
            else:
                return 0 
        else:
            x = x * -1
            temp = str(x)[::-1]
            if ((-1* int(temp)) >= (-(2**31))):
                return (-1*int(temp))
            else:
                return 0        
    
obj = Solution()
print(obj.reverse(1534236469))
        