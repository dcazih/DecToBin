import math

def dec_to_bin(num):
    # 0 in binary is 0
    if num == "0": return 0

    # Ensures only positive input
    if num.isdigit():
        num_len = len(num)
        num = int(num)
    else:
        return -1

    binary_str = ""  # stores the final binary string to be returned
    const_num = num   # stores a constant of num

    # Determines minimum number of bits needed to represent num
    max_exp = math.floor(math.log2(num)) + 1

    # Checks if num can be subtracted by powers of two, and assigns 1 or 0
    for exp in reversed(range(0, max_exp)):
        if num >= 2**exp:
            num -= 2**exp
            binary_str += "1"  # assign 1 if subtraction is possible
        elif const_num > 2**exp:
            binary_str += "0"  # assign 0 if subtraction is not possible

    return binary_str

while True:
    dec_input = input("Decimal to Binary > ")
    print(dec_to_bin(dec_input))
