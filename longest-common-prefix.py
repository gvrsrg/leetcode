class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        proceed = True
        index = 0
        if strs == []:
            return ""
        while proceed:
            if len(strs[0]) < index + 1:
                index += 1
                proceed = False
                break
            letter = strs[0][index]

            for str in strs:
                if len(str)<index+1:
                    proceed = False
                    break
                if str[index] != letter:
                    proceed = False
                    break



            index += 1

        return strs[0][0:index-1]




sol = Solution()
strs = ["flower","flow","flight"]
print(sol.longestCommonPrefix(strs))