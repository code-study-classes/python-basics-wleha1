check_between_numbers = lambda A, B, C: min(A, C) < B < max(A, C)

check_odd_three = lambda number: 100 <= abs(number) <= 999 and number % 2 != 0

check_unique_digits = lambda number: len(set(str(abs(number)))) == 3 if 100 <= abs(number) <= 999 else False


def check_palindrome_number(number):
    s = str(abs(number))
    return s == s[::-1]


check_ascending_digits = lambda number: (
    100 <= abs(number) <= 999 and 
    list(str(number)) == sorted(set(str(number))) and 
    all(x < y for x, y in zip(str(number), str(number)[1:]))
)
