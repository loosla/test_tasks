# Given a sorted array of distinct integers and a target value,
# return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.

# Code to check in main.py
# nums = [1,3,5]
# print(search_insert_position_sorted_arr(nums, 4))

def search_insert_position_sorted_arr(nums: [int], target: int) -> int:
    if not nums:
        return None
    if target in nums:
        return nums.index(target)
    else:
        if target > nums[len(nums)-1]:
            return len(nums)
        elif target < nums[0]:
            return 0
        else:
            return binary_search_to_insert(nums, target)

def binary_search_to_insert(arr, target):
    middle = int(round(len(arr) / 2))
    for i in range(middle):
        if arr[i] < target and arr[i+1] > target:
            return i+1
        elif i > target:
            binary_search_to_insert(arr[:middle], target)
        else:
            binary_search_to_insert(arr[middle:], target)