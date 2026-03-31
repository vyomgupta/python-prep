class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for i,x in enumerate(nums):
            if x in seen:
                return True
            seen.add(x)
        return False