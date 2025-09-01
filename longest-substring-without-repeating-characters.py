class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        if l <= 1:
            return l
        max = 1
        i = 0
        j = 0
        while i + max < l:

            if s[i+max] in s[i:i+max]:
                i += (s[i:i+max].find(s[i+max])+1)
                ss = s[i:i+max]
                maxplastpos = 0
                for letter in ss:
                    if ss.count(letter)>1:
                        lastpos = ss.rfind(letter)
                        if lastpos > maxplastpos:
                            maxplastpos = lastpos
                i += maxplastpos




            else:
                max += 1
        return max

sol = Solution()

s = "ggububgvfk"
res = sol.lengthOfLongestSubstring(s)
print(res)
