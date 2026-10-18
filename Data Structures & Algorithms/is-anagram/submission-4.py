class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_list = [0]*26
        t_list = [0]*26
        for i in s:
            s_list[ord(i) - ord("a")] +=1
        for i in t:
            t_list[ord(i) - ord("a")] += 1
        if s_list == t_list:
            return True
        else:
            return False


