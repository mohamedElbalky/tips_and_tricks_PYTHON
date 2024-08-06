from typing import List


def removeDuplicates(nums: list[int]) -> int:
    s = set(nums)
    nums.clear()
    nums = list(s)
    nums.sort()
    return len(nums)


nums = [1, 1, 2]
print(removeDuplicates(nums))
