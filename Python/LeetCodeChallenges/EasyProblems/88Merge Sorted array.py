from typing import List


class Solution:
    def merge(
        self, numbersOne: List[int], m: int, numbersTwo: List[int], n: int
    ) -> None:
        i, j, k = m - 1, n - 1, m + n - 1

        while i >= 0 and j >= 0:
            if numbersOne[i] >= numbersTwo[j]:
                numbersOne[k] = numbersOne[i]
                i -= 1
            else:
                numbersOne[k] = numbersTwo[j]
                j -= 1
            k -= 1

        while j >= 0:
            numbersOne[k] = numbersTwo[j]
            j -= 1
            k -= 1
