from typing import List

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        for i in range(1, num // 3 + 1):
            consecutive_sum = i + (i + 1) + (i + 2)
            if consecutive_sum == num:
                return [i, i + 1, i + 2]
        return []
