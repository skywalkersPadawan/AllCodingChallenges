class Solution:
    def isPalindrome(self, number: int) -> bool:
        if number < 0:
            return False

        reversedNumber = 0
        originalNumber = number
        while number > 0:
            digit = number % 10
            reversedNumber = reversedNumber * 10 + digit
            number = number // 10

        return reversedNumber == originalNumber
