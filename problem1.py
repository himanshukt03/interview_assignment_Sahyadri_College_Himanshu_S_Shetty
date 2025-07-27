def duplicates(nums):
    for num in nums:
        if nums.count(num) > 1:
            return True
    return False

from problem1_test import test_cases

for nums in test_cases:
    result = str(duplicates(nums)).lower()
    print(f"{nums} -> {result}")
    