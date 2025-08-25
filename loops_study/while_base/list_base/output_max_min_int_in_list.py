#option 1
digits = [12, 5, 27, 67, 9]
index = 0

max_int = digits[0]
min_int = digits[0]

while index < len(digits):
    if digits[index] > max_int:
        max_int = digits[index]
    if digits[index] < min_int:
        min_int = digits[index]
    index = index + 1

print(f'Max sum: {max_int}, min sum: {min_int}')




#option 2
digits = [12, 5, 27, 67, 9]

max_int = max(digits)
min_int = min(digits)

print(f'Max sum: {max_int}, min sum: {min_int}')
