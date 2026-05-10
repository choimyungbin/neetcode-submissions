class Solution:
    def makeHashMap (self, string, hashMap):
        for c in string:
            if c not in hashMap:
                hashMap[c] = 1
            else:
                hashMap[c] += 1
        return hashMap
    def isAnagram(self, s: str, t: str) -> bool:
        hashMapS = {}
        hashMapT = {}

        hashMapS = self.makeHashMap(s, hashMapS)
        hashMapT = self.makeHashMap(t, hashMapT)
        return hashMapS == hashMapT