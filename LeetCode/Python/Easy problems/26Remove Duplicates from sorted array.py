from typing import List


class Solution:
    def removeDuplicates(self, numbers: List[int]) -> int:
        if not numbers:
            return 0

        uniqueIndex = 0
        for i in range(1, len(numbers)):
            if numbers[i] != numbers[uniqueIndex]:
                uniqueIndex += 1
                numbers[uniqueIndex] = numbers[i]
        return uniqueIndex + 1
