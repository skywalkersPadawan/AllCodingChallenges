from typing import List


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        lastSpaceIndex = s.rfind(" ")
        if lastSpaceIndex == -1:
            return len(s)
        else:
            return len(s) - lastSpaceIndex - 1
