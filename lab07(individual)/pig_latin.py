# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Manas Navale
# Section: 577
# Assignment: Lab Topic 7
# Date: 10/9/2023
#
str1 = input("Enter word(s) to convert to Pig Latin: ")
l = str1.split()  # Splitting the input string by spaces, no need for " " inside split
l1 = []

# Loop through the words in the input
for i in l:
    s = i.lower()
    s1 = ""
    if s[0] in ('a', 'e', 'i', 'o', 'u', 'y'):
        s1 = s + "yay"
    else:
        j = 0
        for f in range(len(s)):
            if s[f] in ('a', 'e', 'i', 'o', 'u', 'y'):
                j = f
                break
        for k in range(j, len(s)):
            s1 = s1 + s[k]
        for k in range(0, j):
            s1 = s1 + s[k]
        s1 = s1 + "ay"
    l1.append(s1)

final = ""
# Join the Pig Latin words and print the result
result = " ".join(l1)
print(f"In Pig Latin, \"{str1}\" is:", result)

