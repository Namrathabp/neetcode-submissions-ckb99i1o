from collections import Counter
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # my_dict = defaultdict(list)
        # for i in nums:
        #     my_dict[i].append(i)
        # res = set()
        # for i in my_dict.values():
        #     if len(i) >= k:
        #         res.add(i[0])
        
        # return list(res)
        count_occurences = Counter(nums)
        return heapq.nlargest(k, count_occurences.keys(), key=count_occurences.get)
        