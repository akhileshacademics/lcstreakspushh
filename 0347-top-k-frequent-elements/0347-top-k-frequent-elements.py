import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        return list(dict(sorted(d.items(),key=lambda x:x [1],reverse=True)))[:k]


