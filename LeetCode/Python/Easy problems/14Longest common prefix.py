from typing import List


class Solution:
    def longestCommonPrefix(self, strings: List[str]) -> str:
        if not strings:
            return ""

        prefix = strings[0]
        for s in strings[1:]:
            i = 0
            while i < len(prefix) and i < len(s) and prefix[i] == s[i]:
                i += 1

            prefix = prefix[:i]
            if not prefix:
                break
        return prefix
