
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dis = defaultdict(list)

        for i in strs:
            key = [0] * 26
            for j in i:
                key[ord(j) - ord('a')] += 1
            dis[tuple(key)].append(i)
        return list(dis.values())