# num = [0,0,1,1,1,2,2,3,3,4]
# return : the same list without duplicates

# to main.py
# l = []
# remove_duplicates_sorted_array_in_place.removeDuplicates(l)

# N - Linear Time Complexity
def removeDuplicates(nums):
    for n in range(len(nums)-1, 0, -1):
        if nums[n] == nums[n-1]:
            del nums[n]
    print("removeDuplicates: ")
    print(nums)
    return nums