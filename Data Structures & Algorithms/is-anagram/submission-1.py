class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Complexities: Using hashmap can reduce the complexities to O(n+m) for both.
        # Since orders dont matter in maps, the frequency can be stored and that can be checked.
        mapOne = {}
        mapTwo = {}

        for i in s:
            mapOne[i] = mapOne.get(i, 0) + 1

        for i in t:
            mapTwo[i] = mapTwo.get(i, 0) + 1

        if mapOne == mapTwo:
            return True
        return False