class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumericSet = set(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9'])
        target = []
        # ignore all non-alphanumeric chars ("?", " ")
        # turn into lowercase
        for c in s:
            if c.lower() in alphanumericSet:
                target.append(c.lower())
        # two pointers
        l = 0
        r = len(target)-1
        while l <= r:
            if target[l] != target[r]:
                return False
            l += 1
            r -= 1
        return True