from typing import List


class Solution:
    def addBinary(self, firstVariable: str, secondVariable: str) -> str:
        carry = 0
        result = []

        i, j = len(firstVariable) - 1, len(secondVariable) - 1

        while i >= 0 or j >= 0 or carry:
            intFirstVariable = int(firstVariable[i]) if i >= 0 else 0
            intSecondVariable = int(secondVariable[j]) if j >= 0 else 0

            total = intFirstVariable + intSecondVariable + carry
            carry = total // 2
            currentDigit = total % 2
            # now here we will prepending the current digit to the result
            result.insert(0, str(currentDigit))
            i -= 1
            j -= 1
        return "".join(result)
