"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


durations = {}

for call in calls:
    
	if call[0] in durations:
		durations[call[0]] += int(call[3])
	else:
		durations[call[0]] = int(call[3])
	
	if call[1] in durations:
		durations[call[1]] += int(call[3])
	else:
		durations[call[1]] = int(call[3])

max_duration_nphone_number = None;
max_duration = 0

for key in durations:
	if durations[key] > max_duration:
		max_duration = durations[key]
		max_duration_nphone_number = key


print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_duration_nphone_number,max_duration))