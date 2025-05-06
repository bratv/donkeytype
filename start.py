# A script that is supposed to learn you finding the correct keys, when
# learning to speed type. 
# One key at a time is shown and then you have to hit that key.

# import argparse
import random
import selectorstest
import os
import json

MAX_WIDTH = 40
large_letters = [chr(x) for x in list(range(65,91))]
small_letters = [chr(x) for x in list(range(97,123))]
symbols1 = [chr(x) for x in list(range(91,97))]
symbols2 = [chr(x) for x in list(range(123,127))]
symbols3 = [chr(x) for x in list(range(33,48))]
symbols4 = [chr(x) for x in list(range(58,65))]
symbol_letters = symbols1 + symbols2 + symbols3 + symbols4
error_symbol = '\u2592'
answer_list = []
previous_list = []
wrong_list = []
chosen_chars = []
error_map = {}
beginningui = 0
count = 0
setcount = 5

def init(upper,lower,symbols,custom,number):
    print('initiating letters')
    global chosen_chars
    global setcount
    setcount = number
    chosen_chars = []
    if custom:
        print(custom)
        chosen_chars += list(custom)
    if upper:
        print(upper)
        chosen_chars += large_letters
    if lower:
        print(lower)
        chosen_chars += small_letters
    if symbols:
        print(symbols)
        chosen_chars += symbol_letters
    if not chosen_chars:
        chosen_chars = large_letters + small_letters + symbol_letters
    chosen_chars = set(chosen_chars)
    chosen_chars = list(chosen_chars)

def showUI():
    diff = 0
    if beginningui != 0:
        diff = -1   
    for i in previous_list[beginningui + diff:]:
        print(i,end='')
    print()
    for x in wrong_list[beginningui + diff:]:
        print(x,end='')
    print()
    for x in answer_list[beginningui + diff:]:
        print(x,end='')
    print()

def showEnd():
    l = wrong_list.count(error_symbol)
    print('Errors: ' + str(l))
    for k,v in error_map.items():
        print(k + ':', v)

def addtomap(letter):
    if letter in error_map:
        error_map[letter] += 1
    else:
        error_map[letter] = 1

def handleInput(inp,c):
    if inp == previous_list[len(previous_list) - 1]:
        wrong_list.append(' ')
    else:
        if not ord(inp) == 27:
            addtomap(c)
            wrong_list.append(error_symbol)
    if inp not in chosen_chars:
        answer_list.append(' ')
    else:
        answer_list.append(inp)

def main():
    global beginningui
    global count
    while count < setcount:
        os.system('clear')
        c = random.choice(chosen_chars)
        previous_list.append(c)
        if len(previous_list[beginningui:]) > MAX_WIDTH:
            beginningui += MAX_WIDTH
        showUI()
        inp = selectorstest.mygetch()
        handleInput(inp,c)
        count += 1

        if ord(inp) == 27:
            break
    os.system('clear')
    showUI()
    showEnd()

