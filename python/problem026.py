def divide(numerator, denominator, seen):
  q = numerator / denominator
  r = numerator - (q * denominator)
  if r in seen:
    return len(seen)
  seen.add(r)
  return divide(r * 10, denominator, seen)

def main():
  longest_i = 0
  longest = 0
  for i in xrange(1000, 0, -1):
    if longest > i:
        break
    res = divide(1, i, set())
    if res > longest:
        longest = res
        longest_i = i
  print longest_i, longest

if __name__ == "__main__":
    main()
