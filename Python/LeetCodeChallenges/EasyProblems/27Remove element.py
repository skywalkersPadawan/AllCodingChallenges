from typing import List


class Solution:
    def removeElement(self, numbers: List[int], val: int) -> int:
        if not numbers:
            return 0

        nonMatchingIndex = 0
        for i in range(len(numbers)):
            if numbers[i] != val:
                numbers[nonMatchingIndex] = numbers[i]
                nonMatchingIndex += 1
        return nonMatchingIndex
