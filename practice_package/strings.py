def extract_file_name(full_file_name):
    file_name = full_file_name.replace('\\', '/').split('/')[-1]

    if file_name.startswith('.') and file_name.count('.') == 1:
        return file_name

    return file_name.split('.')[0]


def encrypt_sentence(sentence):
    odds = [sentence[i] for i in range(1, len(sentence), 2)]
    evens = [sentence[i] for i in range(0, len(sentence), 2)]
    
    return ''.join(odds + evens[::-1])


def check_brackets(expression):
    s = expression.replace(' ', '')
    balance = 0

    for idx, ch in enumerate(s):
        if ch == '(':
            balance += 1
        elif ch == ')':
            if balance == 0:
                return idx + 1  
            balance -= 1

    return -1 if balance > 0 else 0


def reverse_domain(domain):
    # Разворачиваем домен
    return '.'.join(domain.split('.')[::-1])


def count_vowel_groups(word):
    w = word.lower()
    vowels = set('aeiou') if len(w) <= 3 else set('aeiouy')  

    count = 0
    in_group = False
    for ch in w:
        if ch in vowels:
            if not in_group:
                count += 1 
                in_group = True
        else:
            in_group = False
    return count
