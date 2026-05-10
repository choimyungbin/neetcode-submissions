class Solution:
    def isPalindrome(self, s: str) -> bool:
        target = []
        # ignore all non-alphanumeric chars ("?", " ")
        # turn into lowercase
        for c in s:
            if c.isalnum():
                target.append(c.lower())
        l = 0
        r = len(target)-1
        while l <= r:
            if target[l] != target[r]:
                return False
            l += 1
            r -= 1
        return True