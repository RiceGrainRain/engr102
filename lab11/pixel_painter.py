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
def convert_to_pixel_art(filename, dark_char):
    with open(filename, 'r') as file:
        lines = file.readlines()

    output_filename = filename.replace('.csv', '.txt')

    with open(output_filename, 'w') as output_file:
        for line in lines:
            values = [int(x) for x in line.strip().split(',')]
            for i in range(len(values)):
                if i % 2 == 0:
                    output_file.write(' ' * values[i])  # Light pixels
                else:
                    output_file.write(dark_char * values[i])  # Dark pixels
            output_file.write('\n')

    print(f"{output_filename} created!")

if __name__ == "__main__":
    input_filename = input("Enter the filename: ")
    dark_character = input("Enter a character: ")

    convert_to_pixel_art(input_filename, dark_character)
