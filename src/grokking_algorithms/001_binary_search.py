"""
Run time: O(log n)
"""


def binary_search(nums: list[int], target: int) -> int | None:
    low = 0
    high = len(nums) - 1

    while high >= low:
        mid: int = int((low + high) / 2)
        guess = nums[mid]
        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return None


def main() -> None:
    my_list = [1, 2, 3, 4, 5, 6, 7]
    print(binary_search(my_list, 1))


if __name__ == "__main__":
    main()
