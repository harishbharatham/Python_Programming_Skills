filename = input("Enter a filename: ").strip()
infile = open(filename, "r")

f = infile.read()
chars = [x for x in f]
words = [x for x in f.split()]
lines = [x for x in f.split('\n')]

print(len(chars), 'Characters')
print(len(words), 'words')
print(len(lines), 'lines')
