from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        prefix = 0
        count = 0

        for num in nums:
            prefix += num

            count += prefix_count[prefix - k]

            prefix_count[prefix] += 1

        return count