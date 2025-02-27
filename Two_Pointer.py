# Two Pointer: IS algorithm Technique, which is used to optimize the time and space complexity, which is used to find the perticular sum of two elements in list, and used to reverse the string.
# Finding a pair with a given sum in a sorted array:
def Two(arr, target):
  left, right =0, len(arr)-1
  while left < right:
    current_sum = arr[left] + arr[right]

    if current_sum == target:
      return True

    elif current_sum < target:
      left += 1

    else:
      right -= 1
  return False

a = int(input("Enter How many Number Of Elements You want:"))
arr = []
for i in range(a):
  b=int(input(":"))
  arr.append(b)
target=int(input("Enter Target Value:"))
print(Two(arr,target))




# Reversing a string using two pointers:
def Two(s):
  s = list(s)
  left, right =0, len(s)-1

  while left < right:
    s[left],s[right] = s[right],s[left]
    left += 1
    right -= 1

  return ''.join(s)

s=input("Enter the String:")
print(Two(s))

--------++++++++++++++++++-----------------------+++++++++++++++++++-------------------+++++++++++++++--------------------++++++++++++++-------------------++++++++++++++++++-----------------+++++++++++++++++--------
