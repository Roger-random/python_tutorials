#!/usr/bin/env python3

#############################################################################
#
# Python string niftiness

# Single and double quotes have same behavior for strings. When using one, the other does not have to be escaped.
print("Isn't it a great day")
print('Isn\'t it a great day')

# The 'r' prefix to a string turns off escaping and \ becomes literal character. (Something Sublime Text doesn't seem to understand...)
print(r'Now I can print a file path c:\windows\system32')

# Triple quotes (both single and double) treats newline in source code as literals to create multiline strings.
# This behavior can be selectively overridden with backslash. (Notice EOL at end of 'print' does not generate a blank line)
print("""\
Usage: thingy [OPTIONS]
    -h              Display this help message
    -H hostname     Host name to connect to
""")

# Strings can be concatenated with '+' and repeated with '*'
print("ba"+"na"*2)

# String indexing!
wound = "It's just a flesh wound"

# Zero based single character is not unusual...
print(wound[0])

# ... but allowing negative numbers is. -1 is the last character, -2 is the second from last, etc.
print(wound[-1])

# String slicing includes index of start but excludes index of end.
print(wound[6:8])

# When omitted, the default uses the start/end of the string.
print(wound[:4])
print(wound[-5:])

# String index out of range will result in error. Slicing index out of range silently defaults to start/end.
print(wound[:42]) # Whereas print(wound[42]) would raise IndexError

#############################################################################
#
# Lists

squares = [1, 4, 9, 16, 25]
palindrome = ['abba', 'tacocat']

# Python lists do not have to be all of the same type, freely concatenable with +
sqpa = squares + palindrome
print(sqpa)

# Append adds to the end
sqpa.append('qwerewq')
print(sqpa)

# Elements can be changed by index or by slicing, replaced, or removed
sqpa[2:6] = ['I replaced many']
print(sqpa)

sqpa[:] = []
print(sqpa)
