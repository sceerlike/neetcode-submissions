class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
       
        hashs = {}
        hasht = {}

        for i in s:
            hashs[i] = hashs.get(i, 0) + 1
        for j in t:
            hasht[j] = hasht.get(j, 0) + 1

        return hashs == hasht

            