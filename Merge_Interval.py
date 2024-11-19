# Merge Interval: It will combine the overlapping intervals in list.


# Given a collection of intervals, merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example:
# Input: [[1, 3], [2, 6], [8, 10], [15, 18]]
# Output: [[1, 6], [8, 10], [15, 18]]

def Merge(intervals):
  intervals.sort(key=lambda x: x[0])    # key=lambda x: x[0] specifies that the list should be sorted based on the first element (x[0]) of each interval.
                                        # The key parameter is useful when: You want to sort complex objects like lists, tuples, or custom objects based on a specific attribute or value.
  merged = []

  for interval in intervals:
    if not merged or merged[-1][1] < interval[0]:
      merged.append(interval)

    else:
      merged[-1][1] = max(merged[-1][1], interval[1])

  return merged

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
result = Merge(intervals)
print(result)



-----++++++-------+++++++-------+++++++------+++++++------++++++++-----------+++++++++-----------
