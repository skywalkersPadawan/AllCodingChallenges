class Solution:
    def romanToInt(self, s: str) -> int:
        romanValues = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        total = 0
        prevValue = 0

        for symbol in reversed(s):
            value = romanValues[symbol]
            if value < prevValue:
                total -= value
            else:
                total += value
            prevValue = value

        return total
