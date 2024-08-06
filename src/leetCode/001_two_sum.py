"""
    problem url: https://leetcode.com/problems/two-sum/description/
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    for i, num in enumerate(nums):
        complement = target - num
        if complement in nums[i+1:]:
            return [i, nums[i+1:].index(complement) + i + 1]

# def two_sum(nums: list[int], target: int) -> list[int]:
#     hashmap = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in hashmap.keys():
#             return [hashmap[complement], i]
#         hashmap[num] = i


def main() -> None:
    nums = [-1, -3, -4, -4, -5]
    target = -8
    # nums = [2, 5, 5, 11]
    # target = 10
    nums = [3, 3]
    target = 6
    print(two_sum(nums, target))


if __name__ == '__main__':
    main()
