matrix = [
    ['P', 'L', 'A', 'N', 'E'],
    ['T', 'C', 'B', 'D', 'F'],
    ['G', 'H', 'I', 'K', 'M'],
    ['O', 'Q', 'R', 'S', 'U'],
    ['V', 'W', 'X', 'Y', 'Z']
]

key = "TCICmI_{_d343_m4}s!s"
flag = ""

for char in key:
    if char.isalpha():
        # Uppercase letters represent row indices
        row_index = ord(char) - ord('A')
    elif char.isdigit() or char.isalnum():
        # Numbers and alphanumeric characters represent column indices
        col_index = int(char)
        flag += matrix[row_index][col_index]

print("Flag:", flag)
