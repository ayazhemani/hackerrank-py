'''
Contiguous Subarrays

You are given an array arr of N integers. For each index i, you are required to determine the number of contiguous subarrays that fulfill the following conditions:
The value at index i must be the maximum element in the contiguous subarrays, and
These contiguous subarrays must either start from or end on index i.

Signature
int[] countSubarrays(int[] arr)

Input
Array arr is a non-empty list of unique integers that range between 1 to 1,000,000,000
Size N is between 1 and 1,000,000

Output
An array where each index i contains an integer denoting the maximum number of contiguous subarrays of arr[i]

Example:
arr = [3, 4, 1, 6, 2]
output = [1, 3, 1, 5, 1]

Explanation:
For index 0 - [3] is the only contiguous subarray that starts (or ends) with 3, and the maximum value in this subarray is 3.
For index 1 - [4], [3, 4], [4, 1]
For index 2 - [1]
For index 3 - [6], [6, 2], [1, 6], [4, 1, 6], [3, 4, 1, 6]
For index 4 - [2]
So, the answer for the above input is [1, 3, 1, 5, 1]

'''

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def count_subarrays(arr):
  # Write your code here
  #Time complexity: O(n)
  output = list()
  forward_array = list()
  back_array = list()
  for i in range(len(arr)):
    output.append(1)
    forward_array = arr[i:len(arr)]
    back_array = arr[:i+1][::-1]

    for j in range(1, len(forward_array)):
      if forward_array[j] > forward_array[0]:
        break
      else:
        output[i] += 1
    for j in range(1, len(back_array)):
      if back_array[j] > back_array[0]:
        break
      else:
        output[i] += 1

  return output

'''
#Time Complexity: O(N^2)


  candidate_sets = dict()
  for i in range(len(arr)):
    for j in range(i+1, len(arr)+1):
      candidate = arr[i:j]
      max_elem = max(candidate)
      if candidate[0] == max_elem or candidate[-1] == max_elem:
        if candidate_sets.get(max_elem) is None:
          candidate_sets[max_elem] = 0
        candidate_sets[max_elem] += 1
  output = []
  for n in arr:
    output.append(candidate_sets[n])

  return output
'''










# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
  print('[', n, ']', sep='', end='')

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  test_1 = [3, 4, 1, 6, 2]
  expected_1 = [1, 3, 1, 5, 1]
  output_1 = count_subarrays(test_1)
  check(expected_1, output_1)

  test_2 = [2, 4, 7, 1, 5, 3]
  expected_2 = [1, 2, 6, 1, 3, 1]
  output_2 = count_subarrays(test_2)
  check(expected_2, output_2)

  # Add your own test cases here
