def string_to_bytes(input_string):
    return bytes.fromhex(input_string)

# Example usage:
input_text = "666c61677b68337834646563696d616c5f63346e5f62335f41424144424142457d"
result = string_to_bytes(input_text)
print(f"The byte sequence of '{input_text}' is:\n {result}")