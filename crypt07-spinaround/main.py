def decrypt_caesar_cipher(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text

ciphertext = "TTZK{Xrzlj_Alczlj_Trvjri}"

for shift in range(26):
    decrypted_message = decrypt_caesar_cipher(ciphertext, shift)
    print(f"Shift {shift:2}: {decrypted_message}")
