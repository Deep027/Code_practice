class Solution:
    def intToRoman(self, num: int) -> str:
        dict_IR = {1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
        den_arr = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        rom_num = ''
        n = len(den_arr)
        for i in range(n-1, -1, -1):
            if num >= den_arr[i]:
                cnt = num // den_arr[i]
                print(f"value of count is {cnt}")
                print(f"value of dict is {dict_IR[den_arr[i]]}")
                if cnt:
                    rom_num = rom_num + cnt*(dict_IR[den_arr[i]])
                num = num - (cnt*den_arr[i])
        return rom_num
    def romanToInt(self, s: str) -> int:
        dict_RI = {"I":1, "IV":4, "V":5, "IX":9, "X":10, "XL":40, "L":50, "XC":90, "C":100, "CD":400, "D":500, "CM":900, "M":1000}
        n = len(s)
        res = 0
        i = 0
        while s[i]:
            if (s[i] + s[i+1]) in dict_RI:
                res += dict_RI[s[i] + s[i+1]]
                i = i + 1
            else:
                res += dict_RI[s[i]]
            i + 1
        print(res)
        return 1

obj = Solution()
print(obj.intToRoman(451))
print(obj.romanToInt("III"))