filename = input("Enter a filename: ").strip()
word = input('Enter a word to remove')
infile = open(filename, "r")

f = infile.read()
words = [x for x in f.split()]
new_words = []

for i in range(len(words)-1):
    if words[i] != word:
        new_words.append(words[i])

file_write = open(filename, 'w')

for word in new_words:
    file_write.write(word)
file_write.close()

print('Done')