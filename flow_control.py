#!/usr/bin/env python3

#############################################################################
#
# Multiple assignments takes everything on left of equal and assigns them
# everything on the right, in order. Demonstrated in this Fibonacci while loop

fib_limit = 20
print("Fibonacci up to", fib_limit)
a,b = 0,1
while b < fib_limit:
  print(b, end=', ')
  a,b = b,a+b
print('(end)')

