class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s,dict_t={},{}
        if len(s) ==len(t):
            pass
        else:
            return False

        return sorted(s)==sorted(t)