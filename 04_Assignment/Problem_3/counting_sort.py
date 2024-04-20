def counting_sort(arr, max_value):
    # Create a count array with a size of the max_value + 1
    count_arr = [0] * (max_value + 1)
    
    # Store the count of each element
    for num in arr:
        count_arr[num] += 1
    
    # Modify count_arr by adding the previous counts (cumulative count)
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]
    
    # Output array to store the sorted elements
    output_arr = [0] * len(arr)
    
    # Place elements into the correct position in the output array
    # and decrease the count by one
    for num in reversed(arr):
        output_arr[count_arr[num] - 1] = num
        count_arr[num] -= 1
    
    return output_arr

def main():
  arr = [4, 2, 2, 8, 3, 3, 3, 12, 0, 1, 5, 2]
  print(f'Input: {arr}')
  max_value = max(arr)
  sorted_arr = counting_sort(arr, max_value)
  print(f'Output after counting sort: {sorted_arr}')
  
if __name__ == "__main__":
  main()