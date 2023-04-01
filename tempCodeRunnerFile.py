S_box = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
]

def substitution_box(decimal_inputs):
    row = int(decimal_inputs[0]+decimal_inputs[5],2)
    col = int(decimal_inputs[1:5],2)
    find_val = S_box[row][col]
    print("Row: ",row," Col: ",col)
    print(find_val)
decimal_inputs = input("Enter binary number: ")
substitution_box(decimal_inputs)