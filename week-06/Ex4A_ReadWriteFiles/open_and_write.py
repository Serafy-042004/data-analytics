f = open("Ex4A_ReadWriteFiles/about_me.txt", "r")

first_50 = f.read(50)
#print(f'{f.readlines()}')
next_four_lines = []

for i in range(4):
    next_four_lines.append(f.readline())

next_100_lines = f.readlines(100)

print("First 50 characters:", first_50)

print("Next four lines, as list by line:", next_four_lines)

print("Next 100 characters, as list by line, rounded up to complete lines:", next_100_lines)

f.close()
