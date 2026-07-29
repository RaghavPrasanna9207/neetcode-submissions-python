class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Here, we can sort the array. Take the first element, everything to it's right will be considered. Use two poiners - one immediately after the element, another at the end. Move the pointers accordingly to get 0. Enumerate to get both indices and values. If the number is greater than zero, break as it won't reach zero. Duplicates have to be accounted for. Add an if condition before the while loop to skip past them, add a while loop during the appending to skip them again.
        # Complexities: O(n^2), O(1)
        
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0: 
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -=1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res