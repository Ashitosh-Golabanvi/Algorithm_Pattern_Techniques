# Sliding Window Approach 
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
