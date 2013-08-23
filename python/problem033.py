
def get_numbers(i):
  ones = i % 10
  tens = i - ones
  res = set([(ones, 10*x) + ones for x in range(1,10)] + [(tens / 10, tens + x) for x in range(10)])
  return res

for i in range(10,100):
  ns = get_numbers(i)
  for x, n in ns:
    if i < n:
      num = i
      den = n
    else:
      num = n
      den = i
    f = num/den


