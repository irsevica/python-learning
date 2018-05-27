# create text file
f = open('data.txt', 'w')

# write to file

f.write('Hello\n')
f.write('World\n')

# close file

f.close()

# Read contents of created file, pass to var and print it

f = open('data.txt')
text = f.read()
for line in open('data.txt'): 
    print(line)


# Play with splitting values
split_text = text.split()
print(split_text)