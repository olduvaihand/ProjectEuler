n = set()
for a in xrange(2, 101):
  for b in xrange(2, 101):
    n.add(a**b)
print len(n)
