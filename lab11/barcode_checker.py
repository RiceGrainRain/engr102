# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Manas Navale
# Section: 577
# Assignment: Lab Topic 11
# Date: 11/15/2023
#

#comment
def check_barcode(str1):
    first_group = 0
    second_group = 0

    for i in range(0, len(str1)-1, 2):
        first_group = first_group + int(str1[i])

    for i in range(1, len(str1)-1, 2):
        second_group = second_group + int(str1[i])

    second_group = second_group * 3
    new_num = first_group + second_group
    last_digit = 10 - (new_num % 10)

    if last_digit == int(str1[-1]):
        return True
    else:
        return False

if __name__ == '__main__':
    filename = input("Enter the name of the file: ")
    valid_barcode_list = []

    with open(filename) as data:
        all_barcode = data.readlines()

        for code in all_barcode:
            code = code.strip()
            if check_barcode(code):
                valid_barcode_list.append(code)

    with open("valid_barcodes.txt", 'w') as f:
        for code in valid_barcode_list:
            f.write(code + "\n")

    print(f"There are {len(valid_barcode_list)} valid barcodes")
