#!/usr/bin/env python3
import random 
import sys
prize_list = ['Goat', 'Goat', 'Car']       # the 3 doors hiding 2 goats and a car
choice_list = [1,2,3]                      # the 3 choices we have
prob = []

choice_list = [x-1 for x in choice_list]
win_tracker_yes_change=[]

for j in range(3):
    for i in range(1,10):
        random.shuffle(prize_list)              # shuffle the goats and a car
        my_choice=random.choice(choice_list)    # randomly choose a door     
        ml= prize_list.copy()    
        del ml[my_choice]                       # eliminate one door hiding a goat and eliminate our first choice (this is the same as swithing)
        if ml[0]=="Goat":
            del ml[0]
        else:
            del ml[1]        
        if 'Car'== ml[0]:                       # check if we won
            win_tracker_yes_change.append(1)    # add 1 if we won
        else:
            win_tracker_yes_change.append(0)    # add 0 if we lost
    prob.append(sum(win_tracker_yes_change)/len(win_tracker_yes_change))

print('%s\t%s' % (prob, 1))
#print('\n\n', 'WINNING PROBABILITY: ', sum(win_tracker_yes_change)/len(win_tracker_yes_change), '\n\n')
# viz_func(win_tracker_yes_change)