#!/usr/bin/env python3

#############################################################################
#
# Multiple assignments takes everything on left of equal and assigns them
# everything on the right, in order. Demonstrated in this Fibonacci while loop

def fib(fib_limit):
  """This is a documentation string (docstring) I should explain my function prints a Fibonacci sequence"""
  print("Fibonacci up to", fib_limit, end=': ')
  a,b = 0,1
  while b < fib_limit:
    print(b, end=', ')
    a,b = b,a+b
  print('(end)')

fib(20)

#############################################################################
# if/elif/else

x = int(input("Enter an integer:"))

if x < 0:
  print("Negative number")
elif x > 0:
  print("Positive number")
else:
  print("Neither negative nor positive, must be zero!")

#############################################################################
# For loops only go over sequences

forseq = ["It's", "a", "happy", "day"]
for w in forseq:
  print(w, len(w))

# To make a for loop that looks like other languages for loops, create a range of integers.
for i in range(5): #for( int i = 0; i < 5; i++)
  print(i)

for i in range(0, 10, 3): #for (int i = 0; i < 10, i+= 3)
  print(i)

#############################################################################
# Python has 'else' block to run after a successfully completed loop

for n in range(2, 10):
  for x in range(2, n):
    if n % x == 0:
      print(n, "equals", x, "*", n/x)
      break;
  else:
    print(n, "is a prime number")