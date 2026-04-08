class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        for i in strs:
            sort_i = "".join(sorted(i))
            my_dict[sort_i].append(i)
        return list(my_dict.values())
        