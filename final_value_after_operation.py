
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0

        for op in operations:
            if "++" in op:
                X += 1
            elif "--" in op:
                X -= 1

        return X
