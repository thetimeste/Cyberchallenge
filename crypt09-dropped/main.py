from itertools import permutations

def generate_block_permutations(input_block):
    # Generate all permutations of the input block
    permuted_blocks = [''.join(p) for p in permutations(input_block)]

    return permuted_blocks

def permute_and_concatenate(input_string, block_size):
    # Ensure that the length of the input string is a multiple of block_size
    if len(input_string) % block_size != 0:
        raise ValueError("Input string length must be a multiple of block_size")

    # Divide the input string into blocks of the specified size
    blocks = [input_string[i:i+block_size] for i in range(0, len(input_string), block_size)]

    # Generate permutations for each block
    permuted_blocks = [generate_block_permutations(block) for block in blocks]

    # Iterate through the permutations and print each concatenation
    for permutation in zip(*permuted_blocks):
        concatenated_result = ''.join(permutation)
        print(concatenated_result)

input_string = "TCICmI_{_d343_m4}s!s"
block_size = 4
permute_and_concatenate(input_string, block_size)
