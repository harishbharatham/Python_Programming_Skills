def displayPermutationHelper(s1, s2):
    if len(s2) == 0:
        print(s1)
    else:
        for i in range(0, len(s2)):
            displayPermutationHelper(s1 + s2[i], s2[0: i] + s2[i+1: ])
            
def displayPermutation(s):
    displayPermutationHelper("", s)
    
displayPermutation('abc')

