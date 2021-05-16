#!/usr/bin/env python3
import random 
import sys
prize_list = ['Goat', 'Goat', 'Car']       
choice_list = [1,2,3]                    
prob = []

choice_list = [x-1 for x in choice_list]
win_tracker_yes_change=[]

try:
    for li in sys.stdin:
        prob = []
        for j in range(int(li)):
            for i in range(1,10000):
                random.shuffle(prize_list)             
                my_choice=random.choice(choice_list)      
                ml= prize_list.copy()    
                del ml[my_choice]                      
                if ml[0]=="Goat":
                    del ml[0]
                else:
                    del ml[1]        
                if 'Car'== ml[0]:                     
                    win_tracker_yes_change.append(1)    
                else:
                    win_tracker_yes_change.append(0)    
            prob.append(sum(win_tracker_yes_change)/len(win_tracker_yes_change))

        print(prob)
except e:
    print(e)