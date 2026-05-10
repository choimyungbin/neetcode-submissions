class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {'(':')', '{':'}', '[':']'}
        for c in s:
            if c in hashMap:
                stack.append(c)
            else:
                if not stack:
                    return False
                opening = stack.pop()
                if hashMap[opening] != c:
                    return False
        if stack:
            return False
        return True
