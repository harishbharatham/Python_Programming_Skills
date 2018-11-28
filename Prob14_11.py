vowels = {'a', 'e', 'i', 'o', 'u'}
filename = input("Enter a filename: ").strip()
infile = open(filename, "r") # Open the file

f = infile.read()
chars = [x for x in f]

Counts = {'vowels': 0,'consonents': 0}

def removeEmptystrings(x):
    modified_chars = []
    for i in range(len(x)):
        if len(chars[i]) != 0 and chars[i].isalnum():
            modified_chars.append(chars[i])
    return modified_chars
chars = removeEmptystrings(chars)

 
for i in chars:
    print(i)
    if i in vowels:
        Counts['vowels'] += 1
    else:
        Counts['consonents'] += 1
print(Counts)
        