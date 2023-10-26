def dec2bin(decimal):
    dec = int(decimal)
    increment = -1
    binary_test_list = []

    # Create a list of possible binary subtractors
    for i in range(int(dec)):
        increment += 1
        binary_test_list.append(2 ** increment)
    binary_test_list.reverse()
    binary_list = []

    # Create binary subtractors
    for bin_nums in binary_test_list:
        if bin_nums <= dec:
            binary_list.append(bin_nums)
    binary_numbers = [0 for i in binary_list]
    increment = -1
    # Convert binary subtractors to binary numbers
    for bin_num in binary_list:
        increment += 1
        if "-" not in str(dec - bin_num):
            dec = dec - bin_num
            binary_numbers[increment] = 1
    binary_string = ""

    # Convert binary numbers to string
    for num in binary_numbers:
        binary_string += str(num)

    if decimal == "0":
        return 0
    else:
        return binary_string

while True:
    dec_input = input("Decimal to Binary > ")
    print(dec2bin(dec_input))
