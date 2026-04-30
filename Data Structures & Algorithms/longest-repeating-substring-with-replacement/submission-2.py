class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charcount = {}
        res = 0
        l = 0
        for r in range(len(s)):
            charcount[s[r]] = charcount.get(s[r], 0) + 1
            while (r-l+1) - max(charcount.values()) > k: #if invalid string
                charcount[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res
        