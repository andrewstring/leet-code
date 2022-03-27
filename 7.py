class Solution:
    def reverse(self, x: int) -> int:
        s = (x > 0) - (x < 0)
        rev = str(x*s)[::-1]
        return int(rev)*s*(int(rev)<2**31-1)

sol = Solution()
print(sol.reverse(-123))