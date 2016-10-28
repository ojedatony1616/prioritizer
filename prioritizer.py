#! /usr/bin/env python3

import random
from random import shuffle
import itertools
from operator import itemgetter

#Initialize the list
items = []

#Take input from user for items to add to priority list
item = 0

while item != "":
	item = input("Enter item to prioritize (leave blank when done): ")
	if item != "":
		items.append(item.strip())

#Initialize a dict to keep score
scores = {x : 0 for x in items}

#Get all the combinations and save them to a list
combos = list(itertools.combinations(items, r=2))
shuffle(combos)

for i in range(len(combos)):
	current = combos[i]
	option_1 = current[0]
	option_2 = current[1]
	answer = input(str(option_1) + " or " + str(option_2) + "? ").strip()
	while answer not in items:
		answer = input(str(option_1) + " or " + str(option_2) + "? ").strip()
	scores[answer] = scores.get(answer, 0) + 1

scores = sorted(scores.items(), key=itemgetter(1), reverse=True)

for x in scores:
	print(str(x[0]) + ": " + str(x[1]))
