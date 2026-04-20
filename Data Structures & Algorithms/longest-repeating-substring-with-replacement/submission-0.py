from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = Counter()
        mx = 0
        l = 0

        for r, char in enumerate(s):
            char_count[char] += 1
            mx = max(mx, char_count[char])
            if r - l + 1 - mx > k:
                char_count[s[l]] -= 1
                l += 1
        return len(s) - l
        