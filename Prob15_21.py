def binary_to_decimal(bstring):
    if not bstring:
        return 0
    return binary_to_decimal(bstring[:-1]) * 2 + int(bstring[-1])



print(binary_to_decimal(input('Enter the binary string:')))

