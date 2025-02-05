# Binary Search Is Nothing But Which Is Used to Search Perticular Element.
# For Performingn Binary Search The Data Should be In Ascending Or Decsending Order.

def Binary(arr, target):
  low = 0
  high = len(arr)
  while low <= high:
    mid = (low+high)//2
    if arr[mid] == target:
      return mid
    elif target < arr[mid]:
      high = mid-1
    else:
      low = mid+1

    return -1

a = int(input("enter the number of values you want to enter as input:"))
arr = []
for i in range(a):
  b = int(input("enter the values:"))
  arr.append(b)
target = int(input("Enter the target value:"))
print(Binary(arr,target))



---------------------------------------------------------+++++++++++++++++++++++++++++++++++++++++++++++++++++----------------------------------------------+++++++++++++++++++++++++++++++++++++
