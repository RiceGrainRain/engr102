# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Cameron Cao
#        Manas Navale
#        Jeremiah Thomas
# Section: 577
# Assignment: Lab8 Team
# Date: 23 10 2023

#commment
#commment
#commment
#commment
#commment
#commment

#take in inputs
print("Enter the time: ", end="")
tim = input()
print("Choose the clock type (12 or 24): ", end="")
typ = int(input())
print("Enter your preferred character: ", end="")
pref = input()
#check if preferred character is permitted
while pref not in "abcdeghkmnopqrsuvwxyz@$&*=":
    print("Character not permitted! Try again: ", end="")
    pref = input()
#split inputs to be used for our dictionaries
split_time = tim.split(":")
hour = split_time[0]
minute = split_time[1]
#split minute into tens and ones digit
minuteten = minute[0]
minuteone = minute[1]
#dictionary for outputs
#have different outputs for each height level of print statements
numbertop = {"1": " 1 ", "2": "222", "3": "333", "4": "4 4", "5": "555", "6": "666", "7": "777", "8": "888", "9": "999", "0": "000", "10": " 1  000", "11": " 1   1 ", "12": " 1  222", "13": " 1  333", "14": " 1  4 4", "15": " 1  555", "16": " 1  666", "17": " 1  777", "18": " 1  888", "19": " 1  999", "20": "222 000", "21": "222  1 ", "22": "222 222", "23": "222 333", "24": "222 4 4", "am": " A  M   M", "pm": "PPP M   M"}
numbermidtop = {"1": "11 ", "2": "  2", "3": "  3", "4": "4 4", "5": "5  ", "6": "6  ", "7": "  7", "8": "8 8", "9": "9 9", "0": "0 0", "10": "11  0 0", "11": "11  11 ", "12": "11    2", "13": "11    3", "14": "11  4 4", "15": "11  5  ", "16": "11  6  ", "17": "11    7", "18": "11  8 8", "19": "11  9 9", "20": "  2 0 0", "21": "  2 11 ", "22": "  2   2", "23": "  2   3", "24": "  2 4 4", "am": "A A MM MM", "pm": "P P MM MM"}
numbermid = {"1": " 1 ", "2": "222", "3": "333", "4": "444", "5": "555", "6": "666", "7": "  7", "8": "888", "9": "999", "0": "0 0", "10": " 1  0 0", "11": " 1   1 ", "12": " 1  222", "13": " 1  333", "14": " 1  444", "15": " 1  555", "16": " 1  666", "17": " 1    7", "18": " 1  888", "19": " 1  999", "20": "222 0 0", "21": "222  1 ", "22": "222 222", "23": "222 333", "24": "222 444", "am": "AAA M M M", "pm": "PPP M M M"}
numbermidbot = {"1": " 1 ", "2": "2  ", "3": "  3", "4": "  4", "5": "  5", "6": "6 6", "7": "  7", "8": "8 8", "9": "  9", "0": "0 0", "10": " 1  0 0", "11": " 1   1 ", "12": " 1  2  ", "13": " 1    3", "14": " 1    4", "15": " 1    5", "16": " 1  6 6", "17": " 1    7", "18": " 1  8 8", "19": " 1    9", "20": "2   0 0", "21": "2    1 ", "22": "2   2  ", "23": "2     3", "24": "2     4", "am": "A A M   M", "pm": "P   M   M"}
numberbot = {"1": "111", "2": "222", "3": "333", "4": "  4", "5": "555", "6": "666", "7": "  7", "8": "888", "9": "999", "0": "000", "10": "111 000", "11": "111 111", "12": "111 222", "13": "111 333", "14": "111   4", "15": "111 555", "16": "111 666", "17": "111   7", "18": "111 888", "19": "111 999", "20": "222 000", "21": "222 111", "22": "222 222", "23": "222 333", "24": "222   4", "am": "A A M   M", "pm": "P   M   M"}

#function to swap characters that make up the ascii clock into the preferred characters inputted
def prefswap(prefchar, prefstring):
    result = ""
    for char in prefstring:
        if char == " ":
            result += char
        else:
            result += prefchar
    return result

print()
#check if there is a preferred character
if pref == "":
    #check which type of clock wanted (12 or 24)
    if typ == 12:
        #check whether its am or pm
        if int(hour) < 12:
            #change 0 o clock to 12
            if int(hour) == 0:
                hour = "12"
            print(numbertop[hour] + "   " + numbertop[minuteten] + " " + numbertop[minuteone] + " " + numbertop["am"])
            print(numbermidtop[hour] + " : " + numbermidtop[minuteten] + " " + numbermidtop[minuteone] + " " + numbermidtop["am"])
            print(numbermid[hour] + "   " + numbermid[minuteten] + " " + numbermid[minuteone] + " " + numbermid["am"])
            print(numbermidbot[hour] + " : " + numbermidbot[minuteten] + " " + numbermidbot[minuteone] + " " + numbermidbot["am"])
            print(numberbot[hour] + "   " + numberbot[minuteten] + " " + numberbot[minuteone] + " " + numberbot["am"])
        else:
            #change time past 12 to 0-12 clock type
            hour = int(hour)
            hour -= 12
            if hour == 0:
                hour = 12
            hour = str(hour)
            print(numbertop[hour] + "   " + numbertop[minuteten] + " " + numbertop[minuteone] + " " + numbertop["pm"])
            print(numbermidtop[hour] + " : " + numbermidtop[minuteten] + " " + numbermidtop[minuteone] + " " + numbermidtop["pm"])
            print(numbermid[hour] + "   " + numbermid[minuteten] + " " + numbermid[minuteone] + " " + numbermid["pm"])
            print(numbermidbot[hour] + " : " + numbermidbot[minuteten] + " " + numbermidbot[minuteone] + " " + numbermidbot["pm"])
            print(numberbot[hour] + "   " + numberbot[minuteten] + " " + numberbot[minuteone] + " " + numberbot["pm"])
            
    else:
        if int(hour) == 0:
                hour = "12"
        if int(hour) <= 9:
            print(numbertop[hour] + "   " + numbertop[minuteten] + " " + numbertop[minuteone])
            print(numbermidtop[hour] + " : " + numbermidtop[minuteten] + " " + numbermidtop[minuteone])
            print(numbermid[hour] + "   " + numbermid[minuteten] + " " + numbermid[minuteone])
            print(numbermidbot[hour] + " : " + numbermidbot[minuteten] + " " + numbermidbot[minuteone])
            print(numberbot[hour] + "   " + numberbot[minuteten] + " " + numberbot[minuteone])
        else:
            #split time into tens and ones digit
            hourten = hour[0]
            hourone = hour[1]
            print(numbertop[hourten] + " " + numbertop[hourone] + "   " + numbertop[minuteten] + " " + numbertop[minuteone])
            print(numbermidtop[hourten] + " " + numbermidtop[hourone] + " : " + numbermidtop[minuteten] + " " + numbermidtop[minuteone])
            print(numbermid[hourten] + " " + numbermid[hourone] + "   " + numbermid[minuteten] + " " + numbermid[minuteone])
            print(numbermidbot[hourten] + " " + numbermidbot[hourone] + " : " + numbermidbot[minuteten] + " " + numbermidbot[minuteone])
            print(numberbot[hourten] + " " + numberbot[hourone] + "   " + numberbot[minuteten] + " " + numberbot[minuteone])
else:
    #check which type of clock wanted
    if typ == 12:
        #check if am or pm
        if int(hour) < 12:
            if int(hour) == 0:
                hour = "12"
            print(prefswap(pref, numbertop[hour]) + "   " + prefswap(pref, numbertop[minuteten]) + " " + prefswap(pref, numbertop[minuteone]) + " " + numbertop["am"])
            print(prefswap(pref, numbermidtop[hour]) + " : " + prefswap(pref, numbermidtop[minuteten]) + " " + prefswap(pref, numbermidtop[minuteone]) + " " + numbermidtop["am"])
            print(prefswap(pref, numbermid[hour]) + "   " + prefswap(pref, numbermid[minuteten]) + " " + prefswap(pref, numbermid[minuteone]) + " " + numbermid["am"])
            print(prefswap(pref, numbermidbot[hour]) + " : " + prefswap(pref, numbermidbot[minuteten]) + " " + prefswap(pref, numbermidbot[minuteone]) + " " + numbermidbot["am"])
            print(prefswap(pref, numberbot[hour]) + "   " + prefswap(pref, numberbot[minuteten]) + " " + prefswap(pref, numberbot[minuteone]) + " " + numberbot["am"])
        else:
            hour = int(hour)
            hour -= 12
            if hour == 0:
                hour = 12
            hour = str(hour)
            print(prefswap(pref, numbertop[hour]) + "   " + prefswap(pref, numbertop[minuteten]) + " " + prefswap(pref, numbertop[minuteone]) + " " + numbertop["pm"])
            print(prefswap(pref, numbermidtop[hour]) + " : " + prefswap(pref, numbermidtop[minuteten]) + " " + prefswap(pref, numbermidtop[minuteone]) + " " + numbermidtop["pm"])
            print(prefswap(pref, numbermid[hour]) + "   " + prefswap(pref, numbermid[minuteten]) + " " + prefswap(pref, numbermid[minuteone]) + " " + numbermid["pm"])
            print(prefswap(pref, numbermidbot[hour]) + " : " + prefswap(pref, numbermidbot[minuteten]) + " " + prefswap(pref, numbermidbot[minuteone]) + " " + numbermidbot["pm"])
            print(prefswap(pref, numberbot[hour]) + "   " + prefswap(pref, numberbot[minuteten]) + " " + prefswap(pref, numberbot[minuteone]) + " " + numberbot["pm"])
            
    else:
        if int(hour) == 0:
                hour = "12"
        if int(hour) <= 9:
            print(prefswap(pref, numbertop[hour]) + "   " + prefswap(pref, numbertop[minuteten]) + " " + prefswap(pref, numbertop[minuteone]))
            print(prefswap(pref, numbermidtop[hour]) + " : " + prefswap(pref, numbermidtop[minuteten]) + " " + prefswap(pref, numbermidtop[minuteone]))
            print(prefswap(pref, numbermid[hour]) + "   " + prefswap(pref, numbermid[minuteten]) + " " + prefswap(pref, numbermid[minuteone]))
            print(prefswap(pref, numbermidbot[hour]) + " : " + prefswap(pref, numbermidbot[minuteten]) + " " + prefswap(pref, numbermidbot[minuteone]))
            print(prefswap(pref, numberbot[hour]) + "   " + prefswap(pref, numberbot[minuteten]) + " " + prefswap(pref, numberbot[minuteone]))
        else:
            hourten = hour[0]
            hourone = hour[1]
            print(prefswap(pref, numbertop[hourten]) + " " + prefswap(pref, numbertop[hourone]) + "   " + prefswap(pref, numbertop[minuteten]) + " " + prefswap(pref, numbertop[minuteone]))
            print(prefswap(pref, numbermidtop[hourten]) + " " + prefswap(pref, numbermidtop[hourone]) + " : " + prefswap(pref, numbermidtop[minuteten]) + " " + prefswap(pref, numbermidtop[minuteone]))
            print(prefswap(pref, numbermid[hourten]) + " " + prefswap(pref, numbermid[hourone]) + "   " + prefswap(pref, numbermid[minuteten]) + " " + prefswap(pref, numbermid[minuteone]))
            print(prefswap(pref, numbermidbot[hourten]) + " " + prefswap(pref, numbermidbot[hourone]) + " : " + prefswap(pref, numbermidbot[minuteten]) + " " + prefswap(pref, numbermidbot[minuteone]))
            print(prefswap(pref, numberbot[hourten]) + " " + prefswap(pref, numberbot[hourone]) + "   " + prefswap(pref, numberbot[minuteten]) + " " + prefswap(pref, numberbot[minuteone]))