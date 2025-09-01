class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        bracket_map = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for br in s:
            if br in bracket_map:
                stack += [br]
            elif not stack or bracket_map[stack.pop()] != br:
                return False

        return stack == []

        proceed = True
        newstr = s
        prevstr = s
        while proceed:
            newstr = newstr.replace("{}", "")
            newstr = newstr.replace("[]", "")
            newstr = newstr.replace("()", "")
            if newstr == prevstr:
                return False
            if newstr=="":
                return True
            prevstr = newstr

        return True






sol = Solution()
s = "()[]{}[]}"
print(sol.isValid(s))