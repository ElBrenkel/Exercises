def two_sum(numbers, target):
    index1 = 0
    index2 = len(numbers) - 1
    while index1 < index2:
        addition = numbers[index1] + numbers[index2]
        if addition == target:
            return [index1, index2]
        elif addition > target:
            index2 -= 1
        else:
            index1 += 1
    return []


nums = [2, 3, 4]
print(two_sum(nums, 6))
