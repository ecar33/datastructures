def merge_sorted_array(A, n, B, m):
  # n is the number of initialized elements in A
  # m is the number of elements in B
  # It's assumed A has enough space (n + m) to hold the merged arrays.
  
  # Index of last element in A
  lastA = n - 1
  
  # Index of last element in B
  lastB = m - 1 
  
  # Index of last postion in A after merge
  merge_index = n + m - 1

  # Merge A and B, starting from the last element in each
  while lastB >= 0:
    if lastA < 0 or A[lastA] < B[lastB]:
      A[merge_index] = B[lastB]
      lastB -= 1
    
    else:
      A[merge_index] = A[lastA]
      lastA -= 1

    merge_index -= 1

# Example usage
def main():
  A = [1, 2, 5] + [0] * 2 # A has a size of 5 with 3 elements initialized
  B = [3, 4] # B has a size of 2, with 2 elements
  print(f"Input: {A}, {B}")
  merge_sorted_array(A, 3, B, 2) # Merge A into B
  print(f"After merge, A is now: {A}") # Print result -> [1, 2, 3, 4, 5]

if __name__ == "__main__":
  main()