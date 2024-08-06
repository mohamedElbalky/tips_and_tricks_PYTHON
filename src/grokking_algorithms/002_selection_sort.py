"""
Run time: O(n^2)
"""

def find_smallest_number(nums: list) -> int:
    smallest_number: int = nums[0]
    smallest_number_index: int = 0
    for i, num in enumerate(nums[1:], 1):
        if num < smallest_number:
            smallest_number = num
            smallest_number_index = i
    return smallest_number_index


def selection_sort(arr: list[int]) -> list[int]:
    sorted_list = []

    while len(arr) > 0:
        smallest_number_index = find_smallest_number(arr)
        small = arr.pop(smallest_number_index)
        sorted_list.append(small)

    return sorted_list


def main() -> None:
    nums: list[int] = [5, 2, 8, 1, 3, 9, 4, 6, 7, 0]
    # print(selection_sort(nums))
    print(selection_sort(nums))


if __name__ == "__main__":
    main()
