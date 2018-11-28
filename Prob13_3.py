from os.path import isfile
filename = input("Enter a filename: ").strip()
infile = open(filename, "r")

scores = [int(n) for n in infile.read().split()]


if isfile(filename):
    total = 0
    for i in scores:
        total += i
    print('There are total ', len(scores), 'scores')    
    print('The total is ', total)
    print('Average is', total/len(scores))
else:
    print('File does not exist')
    