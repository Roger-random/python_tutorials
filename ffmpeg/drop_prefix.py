import os

"""Given a prefix string, examine all the files in the current directory and, 
if a file starts with the prefix, rename the file to remove the prefix."""

prefix="prefix to be removed"

filenames = os.listdir()
filenames.sort() # No functional need for this, just to make things look a little prettier.

for file_from in filenames:
  if file_from.startswith(prefix):
    file_to = file_from[len(prefix):] # String slicing to remove the prefix
    print("Rename from", file_from,"to",file_to)
    os.rename(file_from, file_to)
  else:
    print("Skip",file_from)