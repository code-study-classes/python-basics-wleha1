def check_between_numbers(A, B, C):
    return min(A, C) < B < max(A, C)


def check_odd_three(number):
    return 100 <= abs(number) <= 999 and number % 2 != 0


def check_unique_digits(number):
    return (
        len(set(str(abs(number)))) == 3
        if 100 <= abs(number) <= 999
        else False
    )


def check_palindrome_number(number):
    s = str(abs(number))
    return s == s[::-1]


def check_ascending_digits(number):
    return (
        100 <= abs(number) <= 999 and
        list(str(number)) == sorted(set(str(number))) and
        all(x < y for x, y in zip(str(number), str(number)[1:]))
    )
