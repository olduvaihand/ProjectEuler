
CACHE = {}

def cached(f):
  def wrapper(n):
    res = CACHE[(f, n)] = f(n)
    return res
  return wrapper

@cached
def lower_right(n):
  if n == 1:
    return 0
  return upper_right(n-2) + n-1

@cached
def lower_left(n):
  if n == 1:
    return 0
  return lower_right(n) + n-1

@cached
def upper_left(n):
  if n == 1:
    return 0
  return lower_left(n) + n-1

@cached
def upper_right(n):
  if n == 1:
    return 1
  return n*n

total = 0
for i in xrange(1, 1002, 2):
  total += upper_right(i)
  total += lower_right(i)
  total += lower_left(i)
  total += upper_left(i)
print total
