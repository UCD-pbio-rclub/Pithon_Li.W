#Assignment 2-2
line = input('Line: ')
while line != '':
    first=line.split()
    final=first[::-1]
    break

print(' '.join(final))
