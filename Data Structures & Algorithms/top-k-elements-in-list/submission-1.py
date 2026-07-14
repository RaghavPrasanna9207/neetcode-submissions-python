class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket sort is a technique that involves seperating elements into various buckets.
        # Buckets can be used to sort elements based on their frequencies.

        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1

        # The dict count now has KV pairs of elements and their frequencies. But in order to
        # get k most, an indexed list is needed.

        freq = [[] for i in range(len(nums) + 1)]
        for elem, countElem in count.items():
           freq[countElem].append(elem)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res 