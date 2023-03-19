s_box = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
]

def substitute(decimal_input):
    input_bits = format(decimal_input, '06b')  
    print(decimal_input," In binary:" +input_bits)
    row = int(input_bits[0] + input_bits[5],2)  
    col = int(input_bits[1:5], 2)  
    output_bits = format(s_box[row][col], '04b')  
    return int(output_bits, 2) 

decimal_input = int(input("Enter a decimal number: "))
output_decimal = substitute(decimal_input)
print(output_decimal)  
