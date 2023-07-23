from typing import List


class Solution:
    def mySqrt(self, x: int) -> int:  #  x is non negative integer
        if x == 0:
            return 0

        left, right = 1, x

        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1

        return right
