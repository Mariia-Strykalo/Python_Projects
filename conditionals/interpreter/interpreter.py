def main():
    expression = input("Expression: ").strip()

    x, y, z = expression.split(" ")
    print(calculate(x, y, z))

def calculate(a, b=1, c=2):
    a1 = float(a)
    c1 = float(c)

    if b == "+":
        return round(a1 + c1, 1)
    elif b == "-":
        return round(a1 - c1, 1)
    elif b == "*":
        return round(a1 * c1, 1)
    elif b == "/":
        return round(a1 / c1, 1)
    elif b != "+" or "-" or "*" or "/":
        return "Enter math operator"
    else:
        return "Enter math operator"


main()


#def main():
    #expression = input("Expression: ").strip()
    #x, y, z = expression.split(" ")
    #print(calculate(x, y, z))

#def is_number(value):
    #try:
        #float(value)
        #return True
    #except ValueError:
        #return False

#def calculate(a, b, c):
    #if not (is_number(a) and is_number(c)):
        #return "Enter digits"

    #a = float(a)
    #c = float(c)

    #if b == "+":
        #return round(a + c, 1)
    #elif b == "-":
        #return round(a - c, 1)
    #elif b == "*":
        #return round(a * c, 1)
    #elif b == "/":
        #return round(a / c, 1)
    #else:
        #return "Enter math operator"
