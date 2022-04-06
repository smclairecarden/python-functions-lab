#1
def sum_to(n):
  return sum(range(n+1))
print(sum_to(10))

#2

def largest(li):
  li.sort()
  return li[-1]
print(largest([1, 2, 3, 4, 0]))

#3

def occurences(arg1, arg2):
  # count = 1
  # for n in arg1:
  #   if n == arg2:
  #     count  += 1
  #     return count
  return arg1.count(arg2)
print(occurences('fleep floop', 'oo'))

#4
def product(*args):
  final = 1
  for n in args:
   final *= n
  return final
print(product(2, 5, 5))