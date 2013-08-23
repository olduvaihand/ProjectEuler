import math
import re

CACHE = {}
def cached(f):
  def wrapper(n):
    CACHE[n] = res = f(n)
    return res
  return wrapper

@cached
def is_prime(n):
  if n == 2:
    return True
  if n == 1 or n % 2 == 0:
    return False
  for i in range(3, int(math.sqrt(n))+1, 2):
    if n % i == 0:
      return False
  return True

def truncate(s):
  l = len(s)
  for i in xrange(l):
    yield int(s[i:])
    yield int(s[:l-i])

bad = re.compile(r"[0468]|^1|1$")

def is_truncatable_prime(n):
  nb = buffer(str(n))
  #if bad.search(nb):
  #  return False
  return all(map(is_prime, truncate(nb)))

def main():
  truncatable_primes = [] #37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]
  i = 11
  while len(truncatable_primes) < 11:
    try:
      if is_truncatable_prime(i):
        truncatable_primes.append(i)
      i += 2
    except KeyboardInterrupt:
      print i
  print truncatable_primes, sum(truncatable_primes)

if __name__ == "__main__":
  main()
