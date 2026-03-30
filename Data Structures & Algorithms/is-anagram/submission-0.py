class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapOne = {}
        mapTwo = {}

        for i in s:
            mapOne[i] = mapOne.get(i, 0) + 1

        for i in t:
            mapTwo[i] = mapTwo.get(i, 0) + 1

        if mapOne == mapTwo:
            return True
        return False                