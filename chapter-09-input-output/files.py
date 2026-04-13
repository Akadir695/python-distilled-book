# to read a file at once as string 
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
