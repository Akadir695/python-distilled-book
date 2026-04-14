# to read a file at once as string  to open a file we can absolute path or relative path 
with open('info.txt', 'rt') as file: # 'rt' stands for Read + Text mode.
    data = file.read()
    print(data)
# to read a file line-by-line
with open('info.txt', 'rt') as file:
  for line in file:
    print(line)
# to write to text file 
with open('info.txt', 'wt') as file: # Erases file, starts fresh
  file.write("some output/n")
  print('more output', file=file)
# to append to file 
with open('info.txt', 'at') as file:
    file.write("some more output\n")
# filemodes: the corefiles modes are r(reading) w(writing) and a(appending)
# there are special files x with can be used to write to the file if only the files does not exist.
# with open("specialfile.text", 'x') as file:
#   file.write("this is special file mode")
# Directotories: to get directory listing use os.listdir(pathname)
import os

names = os.listdir(".")  # returns a list of names in the directory
for name in names:
    print(name)
# the print function 
# to print a series values separated by spaces, supply them all to print() likes this 
x = 32
y = 12
z = 90
print('the values are', x, y, z, end='')
for i in range(5):
    print(i, end=' ') # Without end=' ' it would print each number on its own line.
# Output: 0 1 2 3 4
with open('info.txt', 'wt') as f:
  print('the values are', x, y, z, end='', file=f)
# to change the separator character between items, use the sep keyword argument
print('the values are', x, y, z, sep=',')