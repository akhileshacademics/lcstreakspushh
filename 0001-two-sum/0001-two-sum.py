class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i, num in enumerate(nums):
            l = target-num
            if l in hashmap:
                return [hashmap[l],i]
            hashmap[num] = i
        return []



       
