import random


def number_picker():  # picks a randomised number that player must guess
    random_num = ''
    for x in range(0, 3):
        temp = str(random.randrange(0, 9))
        random_num = random_num + temp
    return random_num


### body
fermi_count = 0
bagels_count = 0
check_list = []
check_num = ''
turns = 0
continue_game = False
print('the game has begun.')
random_number = number_picker()
checklist_to_print = {'f': 'fermi', 'p': 'pico', 'b': ' '}
print(random_number)
while turns != 10 and continue_game == False:
    check_list = []
    guess = input(print('please enter a guess'))
    for x in range(0, 3):
        if random_number[0 + x:1 + x] in guess:
            check_num = random_number[0 + x:1 + x]
            if check_num == guess[0 + x:1 + x]:
                check_list.append('f')
                fermi_count = fermi_count + 1
            else:
                check_list.append('p')
        else:
            check_list.append('b')
            bagels_count = bagels_count + 1
    if bagels_count != 3:
        for x in range(0,3):
            print(checklist_to_print.get(check_list[x]), end= ' ')
        print('')
    else:
        print('begal')
    if fermi_count == 3:
        temp2 = input(print('congrats you won \n if yoy would like to go again press y, to end press n'))
        if temp2 == 'n':
            print('game has ended')
            break
    turns = turns + 1
