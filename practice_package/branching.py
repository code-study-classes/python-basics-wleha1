def is_weekend(day): return day in {6, 7}


def get_discount(amount):
    return round(amount * 0.1, 2) if amount >= 5000 else round(amount * 0.05, 2) if amount >= 1000 else 0


def describe_number(n):
    length = "однозначное" if n < 10 else "двузначное" if n < 100 else "трехзначное"
    parity = "четное" if n % 2 == 0 else "нечетное"
    return f"{parity} {length} число"


def convert_to_meters(unitNumber, lengthInUnits):
    factors = {1: 0.1, 2: 1000, 3: 1, 4: 0.001, 5: 0.01}
    return lengthInUnits * factors[unitNumber]


def describe_age(age):
    tens = {
        20: "двадцать", 30: "тридцать", 40: "сорок", 50: "пятьдесят",
        60: "шестьдесят", 70: "семьдесят", 80: "восемьдесят",
        90: "девяносто", 100: "сто"
    }
    ones = {
        1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять",
        6: "шесть", 7: "семь", 8: "восемь", 9: "девять"
    }

    if age % 100 in (11, 12, 13, 14):
        suffix = "лет"
    else:
        suffix = {1: "год", 2: "года", 3: "года", 4: "года"}.get(age % 10, "лет")

    if age <= 20 or age == 100:
        word = tens.get(age, "")
    else:
        ten = (age // 10) * 10
        one = age % 10
        word = tens[ten]
        if one:
            word += " " + ones[one]

    return f"{word} {suffix}"

