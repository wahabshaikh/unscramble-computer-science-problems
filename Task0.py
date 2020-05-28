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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

first_text = texts[0]
incoming_number, answering_number, time = first_text[0], first_text[1], first_text[2]
print("First record of texts, {} texts {} at time {}".format(incoming_number, answering_number, time))


last_call = calls[-1]
incoming_number, answering_number, time, duration = last_call[0], last_call[1], last_call[2], last_call[3]
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(incoming_number, answering_number, time, duration))

