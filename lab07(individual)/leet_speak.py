# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Manas Navale
# Section: 577
# Assignment: Lab Topic 7
# Date: 10/9/2023
#
dictio = {'a': '4', 'e': '3', 'o': '0', 's': '5', 't': '7',}
string = input("Enter some text: ")

# Create a variable to store the leet speak version of the input
leet_speak = ""

for i in string:
    if i.lower() in dictio:
        leet_speak += dictio[i.lower()]
    else:
        leet_speak += i

print(f'In leet speak, "{string}" is:')
print(leet_speak)
