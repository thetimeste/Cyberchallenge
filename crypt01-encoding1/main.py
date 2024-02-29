def decode_to_ascii_array(integers):
    try:
        # Split the input string into individual integers
        integer_list = [int(x) for x in integers.split(',')]
        
        # Decode each integer to its ASCII representation
        decoded_chars = [chr(i) for i in integer_list]
        
        return ''.join(decoded_chars)
    except ValueError:
        return "Invalid input: Not a valid list of ASCII codes."

# Example usage:
input_string = "102, 108, 97, 103, 123, 117, 103, 104, 95, 78, 117, 109, 66, 51, 114, 53, 95, 52, 49, 114, 51, 52, 100, 121, 125"  # ASCII codes for 'A', 'B', 'C'
result = decode_to_ascii_array(input_string)
print(f"The ASCII representation of {input_string} is: \n{result}")
