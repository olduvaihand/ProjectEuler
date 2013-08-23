
total = 0
powers = {str(x): x**5 for x in range(10)}
for i in xrange(10, 5 * 9**5):
  digits = str(i)
  sum_of_digits = sum(powers[d] for d in digits)
  if sum_of_digits == i:
    print i
    total += i
print total
