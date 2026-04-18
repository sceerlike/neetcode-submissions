class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha = "abcdefghijklmnopqrstuvwxyz"

        for i in alpha:
            if s.count(i) != t.count(i):
                return False
        return True

            