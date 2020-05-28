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

total_call_time = dict()

for call in calls:
    incoming_number = call[0]
    answering_number = call[1]
    duration = int(call[3])

    if incoming_number not in total_call_time.keys():
        total_call_time[incoming_number] = 0
    total_call_time[incoming_number] += duration

    if answering_number not in total_call_time.keys():
        total_call_time[answering_number] = 0
    total_call_time[answering_number] += duration

longest_duration = max(total_call_time.items(), key=lambda x: x[1])

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(*longest_duration))