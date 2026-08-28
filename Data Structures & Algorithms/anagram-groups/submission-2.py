class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map ={}

        for strings in strs:
            alpha = [0] * 26
            for c in strings:
                alpha[ord(c) - ord('a')] += 1
            
            key = tuple(alpha)
            if key in hash_map:
                hash_map[key].append(strings)
            else:
                hash_map[key] = [strings]

        return list(hash_map.values())    
        