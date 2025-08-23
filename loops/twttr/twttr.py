#option 1
def main():
    full_word = input("Input: ")
    letters = ["a", "e", "i", "o", "u"]

    result = ""
    for letter in full_word:
        if letter.lower() not in letters:
            result += letter
    print(f"Output: {result}")

main()



#option 2
full_word = input("Input: ")
vowels = "AEIOUaeiou"

result = "".join([L for L in full_word if L not in vowels])
print(f"Output: {result}")



#option 3
full_word = input("Input: ")
vowels = "AEIOUaeiou"

for v in vowels:
    word = full_word.replace(v, "")

print(f"Output: {word}")



#option 4
full_word = input("Input: ")
vowels = "AEIOUaeiou"

table = str.maketrans('', '', vowels)
result = full_word.translate(table)

print(f"Output: {word}")
