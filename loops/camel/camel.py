def main():
    camel_case = input("camelCase: ")
    for letter in camel_case:
        if letter.isupper():
            new = "_" + letter.lower()
            print(new, end="")
        else:
            print(letter, end="")
    print()

main()
