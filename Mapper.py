#!/usr/bin/env python3
import random 
import sys
iteration = 10000

for inp in sys.stdin:
    for j in range(int(inp)):
        win = 0 
        for i in range(1,iteration):
            prize = random.randint(0, 2)       
            my_choice=random.randint(0, 2)                            
            if prize != my_choice:
                    win+=1          
        sys.stdout.write(str(win / iteration)+"\n")