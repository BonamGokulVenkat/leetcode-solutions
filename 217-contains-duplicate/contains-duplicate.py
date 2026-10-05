class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        set1=set()
        for n in nums:
            if n in set1:
                return True
            set1.add(n)
        return False
        