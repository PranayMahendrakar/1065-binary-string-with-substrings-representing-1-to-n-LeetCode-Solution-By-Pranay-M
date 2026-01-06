class Solution:
    def queryString(self, s: str, n: int) -> bool:
        # Check each number from 1 to n
        for i in range(1, n + 1):
            if bin(i)[2:] not in s:
                return False
        return True