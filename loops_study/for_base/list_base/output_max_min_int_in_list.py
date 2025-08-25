#option 1
digits = [12, 5, 27, 67, 9]

max_int = digits[0]
min_int = digits[0]

for i in digits:
    if i > max_int:
        max_int = i
    if i < min_int:
        min_int = i

print(f'Max sum: {max_int}, min sum: {min_int}')



#option 2
digits = [12, 5, 27, 67, 9]

max_int = max(digits)
min_int = min(digits)

print(f'Max sum: {max_int}, min sum: {min_int}')
