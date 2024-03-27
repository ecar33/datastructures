def two_sum(nums, target):
    num_to_index = {}  # Maps numbers to their indices
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return [-1, -1]


target = 9
input1 = [2, 7, 11, 15]
input2 = [15, 2, 7, 11]

print(f'Input: numbers={input1}, target={target}')
print(f'Output: return {two_sum(input1, target)}')
print(f'Input: numbers={input2}, target={target}')
print(f'Output: return {two_sum(input2, target)} ')