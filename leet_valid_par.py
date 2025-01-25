class Solution:
    def isValid(self, s):
        stck = []
        len_s = len(s)
        brak_dict = {"(":")", "[":"]", "{":"}"}
        close_brack = [")", "}", "]"]
        for i in range(len_s):
            if (s[i] in brak_dict):
                stck.append(s[i])
            else:
                if (s[i] in close_brack and len(stck) > 0):
                    if (brak_dict[stck[-1]] == s[i]):
                        stck.pop()
                    else:
                        return False
                else:
                    return False
        if (len(stck) > 0):
            return False
        else:
            return True         

obj = Solution()
print(obj.isValid("()"))
