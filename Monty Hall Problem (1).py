#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


#in the game, the person select door 1 initially

def play_game() :
    global win_ct
    global total_ct
    choose = 1
    M_open = []
    switch = []
    for i in range(1,3):
        M_open.append(i+1)
        switch.append(i+1)
    win = random.randint(1,3)
    if win != 1:
        M_open.remove(win)
    goat = random.choice(M_open)
    switch.remove(goat)
    choose = switch[0]
#     print("In this game, the prize is behind door"+str(win)+\
#           ", Monty opened door"+str(goat)+", so the player switched to door"+str(choose))
    if choose == win:
        win_ct = win_ct + 1
#         print("win")
    total_ct = total_ct + 1


# In[3]:


win_ct = 0
total_ct = 0
for i in range(1000000):
    play_game()
print(win_ct/total_ct)

