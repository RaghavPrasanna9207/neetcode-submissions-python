class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Complexities: O(m * n), O(m), where m is the number of strings and n is the length of the longest string.
        # Anagrams only care about the frequency, not the order. For each string, we can have a tuple with the count of each letter, a frequency array. Then append that with the string to the dictionary to map each array with it's strings. Return the values as a list.
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())