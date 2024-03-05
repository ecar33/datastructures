'''
Lists, Stacks, and Queues
1. (Hint: binary search) For a given sorted list (ascending order) and a target number, find the
first index of this number in O(log n) time complexity. If the target number does not exist in the
list, return -1.
Example 2:
Input: [1, 2, 3, 3, 4, 5, 10]，3
Output: 2
Explanation:
the first index of 3 is 2.

'''

def search(nums, target):
    left, right = 0, len(nums) - 1
    result = -1  # Initialize result as -1 to handle case where target is not found
    
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            result = mid  # Potential first occurrence found
            right = mid - 1  # Move left to find if there's another occurrence to the left
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
            
    return result


nums1 = [1, 2, 3, 3, 4, 5, 10]
target1 = 3
output1 = search(nums1, target1)

nums2 = [1, 1, 2, 3, 3, 4, 5]
target2 = 1
output2 = search(nums2, target2)

nums3 = []
target3 = 0
output3 = search(nums3, target3)

print(f"For {nums1} with target '{target1}', the output is {output1}")
print(f"For {nums2} with target '{target2}', the output is {output2}")
print(f"For {nums3} with target '{target3}', the output is {output3}")
          