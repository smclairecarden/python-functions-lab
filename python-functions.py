#1
def sum_to(n):
  return sum(range(n+1))
print(sum_to(10))

#2
arr = [1, 2, 3, 4, 0]
def largest(li):
  li.sort()
  return li[-1]
print(largest(arr))

#3

def occurences(arg1, arg2):
  count = 1
  for n in arg1:
    if n == arg2:
      count  += 1
      return count
print(occurences('fleep floop', 'fe'))