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

incoming_numbers_call = set()
answering_numbers_call = set()
incoming_numbers_text = set()
answering_numbers_text = set()

for call in calls:
    incoming_numbers_call.add(call[0])
    answering_numbers_call.add(call[1])

for text in texts:
    incoming_numbers_text.add(text[0])
    answering_numbers_text.add(text[0])

telemarketers = incoming_numbers_call - answering_numbers_call - incoming_numbers_text - answering_numbers_text

print("These numbers could be telemarketers: ")
for telemarketer in sorted(telemarketers):
    print(telemarketer)