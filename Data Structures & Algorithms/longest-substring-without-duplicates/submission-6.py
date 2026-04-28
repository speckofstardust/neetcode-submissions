class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #have the current substring in a variable/set
        #slide j if s[j] is not a repeated character
        # calculate length, reset (i,j) if j is the repeating character 
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        i, j = 0, 1
        charset = set()
        charset.add(s[i])
        maxlen = 1
        while j < len(s):
            maxlen = max(maxlen, len(charset))
            while s[j] in charset:
                charset.remove(s[i])
                i += 1
            charset.add(s[j])
            j += 1
        return max(maxlen, len(charset))
            
         