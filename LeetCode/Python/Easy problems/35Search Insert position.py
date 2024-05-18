from typing import List


class Solution:
    def searchInsert(self, numbers: List[int], target: int) -> int:
        left, right = 0, len(numbers) - 1
        while left <= right:
            mid = (left + right) // 2
            if numbers[mid] == target:
                return mid
            elif numbers[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
