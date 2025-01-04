# Slow And Fast Pointer : is Also Known As Tortise And hare algorithm. 
# Which is used to find the middle value of list. and also used to cyhcle detection.

# Problem : Finding Middle Element From Linked-List:

# Finding the Middle of a Linked List:
class Nodelist:
  def __init__(self, value=0, next=None):
    self.value = value
    self.next = next

def findmiddle(head):
  slow = fast = head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

  return slow.value

def Linkedlist(values):
  if not values:
    return None

  head = Nodelist(values[0])
  current = head
  for value in values[1:]:
    current.next = Nodelist(value)
    current = current.next

  return head

a = int(input("Enter How many values you want enter:"))
values = []
for i in range(a):
  b = int(input(":"))
  values.append(b)

head = Linkedlist(values)
mid_value = findmiddle(head)
print("Middle Element:", mid_value)


------------++++++++---------++++++++++----------------++++++++++++++----------------+++++++++++++++-----------------++++++++++++++++-----------------++++++++++++++
