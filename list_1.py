#first_last6
def first_last6(nums):
  if(nums[0] == 6 or nums[len(nums)-1] == 6):
    return True
  return False

#same_first_last
def same_first_last(nums):
  '''
  nums: an array of ints
  
  returns: True if array is length 1 or more and first element = last element
  '''
  return (len(nums) >= 1 and nums[0] == nums[-1])

#make_pi
def make_pi():
  list = [3, 1, 4]
  return list

#common_end
def common_end(a, b):
  '''
  a: an array of ints
  b: an array of ints
  
  returns: True if they have same first element or last element
  '''
  return (a[0] == b[0] or a[-1] == b[-1])

#sum3
def sum3(nums):
  return nums[0] + nums[1] + nums[2]

#rotate_left3
def rotate_left3(nums):
  x = nums[0]
  nums[0] = nums[1]
  nums[1] = nums[2]
  nums[2] = x
  return nums

#reverse3
def reverse3(nums):
  nums.reverse()
  return nums

#max_end3
def max_end3(nums):
  if(nums[0] > nums[-1]):
    nums[1] = nums[0]
    nums[2] = nums[0]
    return nums
  else:
    nums[0] = nums[-1]
    nums[1] = nums[-1]
    return nums
  
#sum2
def sum2(nums):
  if(len(nums) >= 2):
    return nums[0] + nums[1]
  elif(len(nums) == 1):
    return nums[0]
  return 0

#middle_way
def middle_way(a, b):
  array = []
  array.append(a[1])
  array.append(b[1])
  return array

#make_ends
def make_ends(nums):
  return [nums[0], nums[-1]]

#has23
def has23(nums):
  return (2 in nums or 3 in nums)
