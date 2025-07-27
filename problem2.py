def shift_zeroes(nums):
    insert_pos = 0

    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1

    for i in range(insert_pos, len(nums)):
        nums[i] = 0

from problem2_test import test_cases

for nums in test_cases:
    original = nums.copy()
    shift_zeroes(nums)
    print(f"{original} -> {nums}")