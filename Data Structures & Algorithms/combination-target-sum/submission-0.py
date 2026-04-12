class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return

            cur.append(nums[i]) #try with this number
            dfs(i, cur, total + nums[i]) #now the total is increased as
            #we have already added a number

            cur.pop() #we are here if the total exceeded OR there is no more
            #to explore. so we remove the last element
            dfs(i + 1, cur, total) #move on without the last element

        dfs(0, [], 0)
        return res