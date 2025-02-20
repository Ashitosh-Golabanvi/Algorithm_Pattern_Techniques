# Sliding Window Algorithm Approach : Is problem solving technique, which will optimize the time and space complexity, which is used when we need to evaluate the subarrays or substrings.
# Problem Statement: Given an array of integers and a number k, find the maximum sum of any contiguous subarray of size k.

 def Slide(arr, k):
  n = len(arr)
  if n < k:
    return None

  max_win = sum(arr[:k])
  maxe = max_win

  for i in range(k, n):
    max_win += arr[i] - arr[i-k]
    maxe = max(maxe, max_win)

  return maxe

a=int(input("How Many Values You Want Enter:"))
arr=[]
for i in range(a):
  b=int(input("Enter The values:"))
  arr.append(b)
k = int(input("Enter Number Of Slide Value:"))
print(Slide(arr, k))







# Problem Statement: Given a string, find the length of the longest substring without repeating characters.
def Long(s):
  char_set = set()
  left = 0
  max_len = 0

  for right in range(len(s)):
    while s[right] in char_set:
      char_set.remove(s[left])
      left += 1

    char_set.add(s[right])
    max_len = max(max_len, right - left +1)
  return max_len

s = input("Enter value:")
print(Long(s))


--------------------++++++++++++++++-------------------++++++++++++++++++++-----------------++++++++++++++++------
