EXPANSION_TABLE = [
    31,  0,  1,  2,  3,  4,  3,  4,  5,  6,  7,  8,  7,  8,  9, 10,
    11, 12, 11, 12, 13, 14, 15, 16, 15, 16, 17, 18, 19, 20, 19, 20,
    21, 22, 23, 24, 23, 24, 25, 26, 27, 28, 27, 28, 29, 30, 0,  31,
]

def expand(input_block):
    expanded_block = [0] * 48
    for i in range(48):
        expanded_block[i] = input_block[EXPANSION_TABLE[i]]
    return expanded_block

input_block = [
    1, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 0,
    0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 1
]

expanded_block = expand(input_block)

print(expanded_block)
