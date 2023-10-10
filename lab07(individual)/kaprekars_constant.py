# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Manas Navale
# Section: 577
# Assignment: Lab Topic 7
# Date: 10/9/2023
#
x = int(input("Enter a four-digit integer: "))

if x == 6174:
    print(f"{x} > 0")
    print(f"{x} reaches 0 via Kaprekar's routine in 0 iterations")
else:
    number = f"{x:04d}"
    count = 0

    while number != '6174' and number != '0000':
        n1 = ''.join(sorted(number))
        n2 = ''.join(reversed(n1))
        n = int(n2) - int(n1)
        print(f"{int(number):d} > ", end='')
        number = f"{n:04d}"
        #count 
        count += 1

    if number == '6174':
        print('6174')
        print(f"{x} reaches 6174 via Kaprekar's routine in {count} iterations")
    else:
        print('0')
        print(f"{x} reaches 0 via Kaprekar's routine in {count} iterations")
