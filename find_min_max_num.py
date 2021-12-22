# findding minimum number first
def find_min(arr):
  size = len(arr) # we need size of an array to traverse through given array
  min = 1000000000000000   # we will set min var to the largest number possible.
  for i in range(size):
    if arr[i] < min:
      min = arr[i]
  return min

def find_max(arr):
  size = len(arr)
  max = 0
  for i in range(size):
    if arr[i] > max:
      max = arr[i]
  return max

arr = [98, 76, 43 , 9, 79]
print(find_min(arr))
print(find_max(arr))


# if the min var is too lame in this code we can just find the max number first and replace 10000000... with max number. 
