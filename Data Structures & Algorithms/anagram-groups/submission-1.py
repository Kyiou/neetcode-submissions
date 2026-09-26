class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort un string pour verifier les anagrams
        strs_dict = defaultdict(list)
        for s in strs:
            sorted_str = ''.join(sorted(s))
            strs_dict[sorted_str].append(s)
        return list(strs_dict.values())