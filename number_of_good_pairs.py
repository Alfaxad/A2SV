class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)

        # Use two for loops to compare each pair of elements
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    result += 1

        return result
