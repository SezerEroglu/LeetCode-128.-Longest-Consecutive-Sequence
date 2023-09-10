from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums = sorted(nums)
        longest = 1
        current = 1

        for i in range(1, len(nums)):
            if nums[i - 1] + 1 == nums[i]:
                current += 1
            elif nums[i - 1] == nums[i]:
                continue
            else:
                longest = max(longest, current)
                current = 1

        longest = max(longest, current)
        return longest
