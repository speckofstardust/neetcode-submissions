class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #fixed window problem?
        for i in range(len(s2)-len(s1)+1):
            if self.isPerm(s1, s2[i: i+len(s1)]):
                return True 
        return False
    def isPerm(self, s1: str, s2:str) -> bool:
        return sorted(s1) == sorted(s2)
        