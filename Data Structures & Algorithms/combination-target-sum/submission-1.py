class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # Sort all the numbers first. Then, use DFS to check if the list is a valid list, append it if so, and then take a for loop, and consider everything from the next element onwards, recursively DFSing. Then pop and backtrack.

        # Complexities: O(2^(t/m)), O(t/m) where t is the given target and m is the minimum value in the given array.
        res = []
        nums.sort()

        def dfs(i, cur, total):
            if target == total:
                res.append(cur.copy())
                return

            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                cur.append(nums[j])
                dfs(j, cur, total + nums[j])
                cur.pop()

        dfs(0, [], 0)
        return res