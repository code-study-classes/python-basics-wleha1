def count_char_occurrences(text):
    counts = {}
    hyphen_count = 0
    for ch in text.lower():
        if ch == '-':
            hyphen_count += 1
        elif 'a' <= ch <= 'z':
            if ch in counts:
                counts[ch] += 1
            else:
                counts[ch] = 1

    if hyphen_count > 0:
        vowels = ['a', 'e', 'i', 'o', 'u']
        for letter in list(counts.keys()):
            if letter not in vowels:
                counts[letter] -= hyphen_count
                if counts[letter] <= 0:
                    del counts[letter]

    return counts


def merge_dicts(dict1, dict2, conflict_resolver):
    result = {}
    for k, v in dict1.items():
        result[k] = v

    for k, v2 in dict2.items():
        if k in result:
            v1 = result[k]
            result[k] = conflict_resolver(k, v1, v2)
        else:
            result[k] = v2

    return result


def invert_dictionary(original_dict):
    inverted = {}
    for k in original_dict:
        v = original_dict[k]
        if v in inverted:
            inverted[v].append(k)
        else:
            inverted[v] = [k]
    return inverted


def dict_to_table(data_dict, columns):
    headers = [col.upper() for col in columns]

    widths = []
    for i, col in enumerate(columns):
        max_w = len(headers[i])
        for entry in data_dict.values():
            val_str = str(entry[col]) if col in entry else "N/A"
            if len(val_str) > max_w:
                max_w = len(val_str)
        widths.append(max_w)

    header_cells = [" " + headers[i].ljust(widths[i]) + " " for i in range(len(columns))]
    header_row = "|" + "|".join(header_cells) + "|"
    sep_row = "|" + "|".join("-" * (widths[i] + 2) for i in range(len(columns))) + "|"

    data_rows = []
    for entry in data_dict.values():
        cells = []
        for i, col in enumerate(columns):
            val_str = str(entry[col]) if col in entry else "N/A"
            cells.append(" " + val_str.ljust(widths[i]) + " ")
        data_rows.append("|" + "|".join(cells) + "|")

    return "\n".join([header_row, sep_row] + data_rows)


def deep_update(base_dict, update_dict, top_level=True):
    result = {}
    for k, v in base_dict.items():
        result[k] = v

    common = []
    for k in base_dict:
        if k in update_dict:
            common.append(k)

    if not common:
        return result

    for k, upd_val in update_dict.items():
        if k in base_dict:
            base_val = base_dict[k]
            if isinstance(base_val, dict) and isinstance(upd_val, dict):
                result[k] = deep_update(base_val, upd_val, False)
            else:
                result[k] = upd_val
        else:
            if top_level:
                result[k] = upd_val

    return result
