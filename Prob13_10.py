class Rational:
    def __init__(self, numerator = 0, denominator = 1):
        if denominator == 0:
            raise RuntimeError("Denominator cannot be zero")
              
        self.numerator = numerator
        self.denominator = denominator

def main():
    r1 = Rational()
    print("Default values: ", r1.numerator, r1.denominator)
    try:
        r2 = Rational(9,0)
    except RuntimeError as re:
        print(re)
        
main()
