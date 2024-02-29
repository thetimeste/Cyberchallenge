def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def hex_to_bytes(hex_string):
    return bytes.fromhex(hex_string)

def brute_force_one_byte_key(ciphertext):
    ciphertext_bytes = hex_to_bytes(ciphertext)
    
    for key in range(256):  # Iterate through all possible one-byte keys (0-255)
        # Build a key of the same length as the ciphertext (repeating key)
        key_bytes = bytes([key] * len(ciphertext_bytes))

        decrypted_text = xor_bytes(ciphertext_bytes, key_bytes)
    
        print(f"Key: {key:02X}, Decrypted Text: {decrypted_text.decode('utf-8', 'ignore')}")

ciphertext = "104e137f425954137f74107f525511457f5468134d7f146c4c"

brute_force_one_byte_key(ciphertext)
