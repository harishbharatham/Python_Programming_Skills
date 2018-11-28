def binaryToHex(binaryValue):
    decimalValue = binaryToDecimal(binaryValue)
    hex = decimalToHex(decimalValue)
    return hex   
    
def decimalToHex(decimalValue):
    hex = " "
    while decimalValue != 0:
        hexvalue = decimalValue % 16
        hex = toHexChar(hexvalue) + hex
        decimalValue = decimalValue // 16
    return hex
 
def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord('0'))
    else:
        return chr(hexValue - 10 + ord('A'))
    
def binaryToDecimal(binaryValue):
    decimal = 0
    for i in range(0,len(binaryValue)):
        ch = binaryValue[i]
        decimal = decimal + int(ch)*2**(len(binaryValue)-1-i)
    return decimal
        
def main():
    binaryValue = input("Enter a binary number: ").strip()
    hexValue = binaryToHex(binaryValue)
    print("The Hex value for the binary is :", hexValue)
 
main()
