def is_identifier_char(char):
    return char.isalnum() or char == "_"


def extract_tokens_with_positions(source_code):
    tokens = []

    line = 1
    column = 1
    i = 0

    while i < len(source_code):
        char = source_code[i]

        if char == "\n":
            line += 1
            column = 1
            i += 1
            continue

        if char.isalpha() or char == "_":
            start_line = line
            start_column = column
            token = ""

            while i < len(source_code) and is_identifier_char(source_code[i]):
                token += source_code[i]
                i += 1
                column += 1

            tokens.append({
                "token": token,
                "line": start_line,
                "column": start_column
            })

            continue

        i += 1
        column += 1

    return tokens