def calculate_distance(x1, x2):
    return abs(x1 - x2)


def calculate_segments(length_a, length_b):
    return length_a // length_b


def calculate_digit_sum(number):
    return sum(int(d) for d in str(abs(number)))


def calculate_rect_area(x1, y1, x2, y2):
    return abs((x2 - x1) * (y2 - y1))


def round_to_multiple(number, multiple):
    return round(number / multiple) * multiple
