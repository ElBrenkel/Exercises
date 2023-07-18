def longest_consecutive(nums: list):
    nums_set = set(nums)
    max_sequence = 0
    nums.sort()
    for num in nums_set:
        if num - 1 not in nums_set:
            temp_length = 0
            while num + temp_length in nums_set:
                temp_length += 1
            max_sequence = max(temp_length, max_sequence)
    return max_sequence


numbers = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(longest_consecutive(numbers))
