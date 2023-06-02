import random
from statistics import multimode
import math

global months_29
global months_30
global months_31
global month_to_int
###### initialisation of values ########################
days = []  # creates a list of 31 values for random function
for x in range(1, 32):  # to be applied on it
    days.append(x)  #

months_30 = ['April', 'June', 'September', 'November']
months_31 = ['January', 'March', 'May', 'July', 'August', 'October', 'December']
months_29 = ['February']
month_to_int = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8,
                'September': 9, 'October': 10, 'November': 11, 'December': 12}
index = 0


########################################################

def generate_bday(day: list):  # picks a day and month
    rday = random.choice(day)
    if rday <= 29:
        rmonth = random.choice(months_29 + months_30 + months_31)
        rmonth = month_to_int[rmonth]
    elif rday == 30:
        rmonth = random.choice(months_30 + months_31)
        rmonth = month_to_int[rmonth]
    else:
        rmonth = random.choice(months_31)
        rmonth = month_to_int[rmonth]

    return rday, rmonth


def find_duplicates(blist):
    duplicates = []
    for i in range(len(blist)):
        if blist[i] in blist[i + 1:] and i not in duplicates:
            duplicates.append(i)
    return duplicates


def select_bdays(counter):  # generate list with all bdays
    day = []
    month = []
    birth_DM = []
    for y1 in range(0, counter):
        day.append(0)
        month.append(0)
        birth_DM.append(0)
    for y2 in range(0, counter):
        month[y2], day[y2] = (generate_bday(days))
        birth_DM[y2] = str(day[y2]) + str(month[y2])
    return birth_DM, month, day


def month_in_name(val):  # turn the value of a dict into its key
    for key, value in month_to_int.items():
        if val == value:
            return key


####BODY################################################
dup_count = 0
valcheck = False
print('The simulation has begun\nPlease enter the number of birthdays to simulate?')
count = int(input())
print('the simulation will now begin collecting data for', count, 'birthdays')
print('would you like to see the selection? \nenter \'yes\' to see else enter \'no\' ')
choice = input()

if choice == 'yes' or choice == 'no':
    valcheck = True
while valcheck != True:
    print('error in the value inputted please enter either \'yes\' or \'no\'. no other value can be accepted')
    print('would you like to see the selection? \nenter \'yes\' to see else enter \'no\' ')
    choice == input()
    if choice == 'yes' or choice == 'no':
        valcheck = True
for x in range(0, count):
    if choice == 'yes':
        bday, bmonth = (generate_bday(days))
        mon = month_in_name(bmonth)
        print(bday, mon[:3], end=',')

birth_dayANDmonth, birth_month, birth_day = select_bdays(count)
index = find_duplicates(birth_dayANDmonth)
print('for the given range of birthdays same values were observed at', end=' ')

if len(index) == 1:
    print(birth_day[index[0]], month_in_name(birth_month[index[0]]))
elif len(index) > 1:
    for z in range(0, len(index)):
        print(birth_day[index[z]], (month_in_name(birth_month[index[z]])), end=',')

for x in range(0, 1):
    if x % 10_000 == 0:
        print('simulated ', x, ' values')
    birth_dayANDmonth = select_bdays(count)
    index = find_duplicates(birth_dayANDmonth)
    dup_count = len(index)

probability = (dup_count / 100_000) * 100
print('probability is:', round(probability, 2), '%')
