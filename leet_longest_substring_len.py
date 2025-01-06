class Solution:
    # def get_substring(self, stng):
    #     arr = []
    #     for i in range(len(stng)):
    #         for j in range(i+1, len(stng)+1, 1):
    #             arr.append(stng[i:j])
    #     return arr
    
    # def remove_index(self, ary):
    #     bad_indx = []
    #     for j in ary:
    #         temp = set(j)
    #         bad_indx.append(temp)
    #     return bad_indx

    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        lf_ptr = 0
        final = 0
        for lf_ptr in range(n):
            char_set = set()
            for rt_ptr in range(lf_ptr, n):
                if s[rt_ptr] in char_set:
                    break
                else:
                    char_set.add(s[rt_ptr])
                    new_len = len(char_set) # 1
            if new_len > final:
                final = new_len
        return final
    
    def lengthOfLongestSubstring_2(self, s: str) -> int:
        start = -1
        max_length = 0
        hash_table: dict[str, int] = dict()

        for index, char in enumerate(s):
            if char in hash_table and (_index := hash_table[char]) > start:
                start = _index
                hash_table[char] = index
            else:
                hash_table[char] = index
                max_length = max(index - start, max_length)

        return max_length

obj = Solution()
print(obj.lengthOfLongestSubstring('pwwkew'))
#print(obj.lengthOfLongestSubstring('abcabcbb'))