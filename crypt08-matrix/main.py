def find_position(matrix, char):
    # Find the position of a character in the matrix
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == char:
                return i, j

def playfair_decrypt(ciphertext, matrix):
    decrypted_text = ""
    for i in range(0, len(ciphertext)-1, 2):
        pair = ciphertext[i:i+2]
        row1, col1 = find_position(matrix, pair[0])
        row2, col2 = find_position(matrix, pair[1])

        if row1 == row2:
            decrypted_text += matrix[row1][(col1-1) % 5] + matrix[row2][(col2-1) % 5]
        elif col1 == col2:
            decrypted_text += matrix[(row1-1) % 5][col1] + matrix[(row2-1) % 5][col2]
        else:
            decrypted_text += matrix[row1][col2] + matrix[row2][col1]

    return decrypted_text

# Example usage:
key_matrix = [
    ['P', 'L', 'A', 'N', 'E'],
    ['T', 'C', 'B', 'D', 'F'],
    ['G', 'H', 'I', 'K', 'M'],
    ['O', 'Q', 'R', 'S', 'U'],
    ['V', 'W', 'X', 'Y', 'Z']
]

ciphertext = "CGKRKRLANXBERXBHLGAUVSZMQODKGB"
decrypted_message = playfair_decrypt(ciphertext, key_matrix)
print(f"Decrypted Message: {decrypted_message}")
