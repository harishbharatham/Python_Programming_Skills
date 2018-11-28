def main():
    # Prompt the user to enter a file
    filename = input("Enter a filename: ").strip()
    infile = open(filename, "r") # Open the file
    wordCounts = {}
    for line in infile:
        processLine(line.lower(), wordCounts)
    print(wordCounts)

# Count each word in the line
def processLine(line, wordCounts):
    line = replacePunctuations(line) # Replace punctuation with space
    # Get words from each line
    words = line.split()
    for word in words:
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1
    return wordCounts

# Replace punctuation in the line with a space
def replacePunctuations(line):
    for ch in line:
        if ch in "~@#$%^&*()_-+=~<>?/,.;:!{}[]|'\"":
            line = line.replace(ch, ' ')
            return line
        
main() # Call the main function