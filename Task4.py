"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

marketing_map = {}
marketing_list = []

for call in calls:
	if marketing_map.get(call[0], None) == None:
		marketing_map[call[0]] = True

	if marketing_map.get(call[1],None) == True:
		marketing_map[call[1]] = False

for text in texts:
	if marketing_map.get(text[0]) == True:
		marketing_map.get(text[0])

	if marketing_map.get(text[1]) == True:
		marketing_map.get(text[1])

for num in marketing_map:
	if marketing_map[num]:
		marketing_list.append(num)

print("These numbers could be telemarketers: ")
for num in sorted(marketing_list):
	print(num)










