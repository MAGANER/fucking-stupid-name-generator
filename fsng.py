# -*- coding: utf-8 -*-
from random import *

regime_of_work = input("say ass or boobs?") # :D

while regime_of_work != "ass" or regime_of_work != "boobs":
    regime_of_work = input("say ass or boobs?")
    if regime_of_work == "ass" or regime_of_work == "boobs":
        break
    

number_of_names = 0 # that will be used to create new world
names = []     # contains all names
names_to_use = [] # this list contains names that will be used
               # to create new world
processed_names = [] # concatinete all strings and get result of
                     # script

# enter names
while 1:
    name = input("enter name:")
    if name =='':
        break
    names.append(name)

list_size = len(names) # get number of all names

number_of_names = randint(0, list_size)

# less number of names is 2
if number_of_names == 1:
    number_of_names+=1

# take random names from list
if regime_of_work == "boobs":
    while number_of_names > 0:
        if regime_of_work == "boobs":
            _name = choice(names)
            # check if this name is already took
            for word in names_to_use:
                if word == _name:
                    continue
    
            names_to_use.append(_name)
            number_of_names -=1
if regime_of_work == "ass":
    for word in names:
        names_to_use.append(word)

for word in names_to_use:
    processed_name = ""

    # it means get position of start char in word
    # also script does to find end word char

    start_word_char = randint(0, len(word))
    end_word_char = randint(start_word_char, len(word))
    
    if start_word_char == 0:
        start_word_char = randint(0, len(word))
    if end_word_char == 0:
        end_word_char = randint(start_word_char, len(word))

    # set word
    i = start_word_char
    y = end_word_char
    if i > y:
        i = end_word_char
        y = start_word_char
    while i != y:
        processed_name+=word[i]
        i+=1
    processed_names.append(processed_name)

# concatinete all words
final_word = ""
for word in processed_names:
    final_word+=word
print(final_word)