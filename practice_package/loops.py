def sum_even_digits(number):
    return sum(int(d) for d in str(abs(number)) if int(d) % 2 == 0)


def count_vowel_triplets(text: str) -> int:
    vowels = set('aeiouy')
    s = text.lower()
    n = len(s)
    count = 0
    i = 0

    while i < n:
        if s[i] in vowels:
            start = i
            while i < n and s[i] in vowels:
                i += 1
            L = i - start

            if L < 3:
                continue
            if L == 3 or start == 0 or i == n:
                count += 1
            else:
                count += L - 3
        else:
            i += 1

    return count


def find_fibonacci_index(number):
    a, b, index = 1, 1, 2
    if number == 1:
        return 1
    while b < number:
        a, b = b, a + b
        index += 1
    return index if b == number else -1


def remove_duplicates(string):
    if not string:
        return ""
    result = [string[0]]
    for c in string[1:]:
        if c != result[-1]:
            result.append(c)
    return ''.join(result)
