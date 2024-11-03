***Cyclic Sort:*** which is basically sorting algorithm.
* It starts from Initial Element.
* And Checks the current element is at right place or not.
* If It's Not in Right Place, then It will swap the current element to currect place.
* this process repeats until all the elements should place at right place or until end of array elements.


** Conditions:**
* The major Drowback Of This Pattern is the Given elements of inputs should be Naughbor Elements
* The Input values should be under the number of value, Like : We want to give 6 Inputs, The Values should Be Under The 6 Numbers For this case Only It Will work.


* Ex: I/P: 3,1,5,4,2
* Like this Inputs won't work: 5,6,1,8,10


def Cycle(arr):
  i = 0

  while i < len(arr):
    correct_index = arr[i] - 1

    if arr[i] != arr[correct_index]:
      arr[i], arr[correct_index] = arr[correct_index], arr[i]

    else:
      i += 1


  return arr



a = int(input("Enter How many Number of elements you want enter:"))
arr = []
for i in range(a):
  b = int(input("ENter The Values:"))
  arr.append(b)
sorted_arr = Cycle(arr)
print("Sorted_Values:", sorted_arr)


--------------------------------;;;;;;;;----------------------------------
