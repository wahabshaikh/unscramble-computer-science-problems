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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A

bangalore_fixed_line = '(080)'
area_codes = list()

for call in calls:
	incoming_number = call[0]
	answering_number = call[1]

	if incoming_number.startswith(bangalore_fixed_line):
		if answering_number.startswith('('):
			start = 1
			end = answering_number.find(')')
			area_codes.append(answering_number[start:end])

		elif answering_number.startswith('7') or answering_number.startswith('8') or answering_number.startswith('9'):
			area_codes.append(answering_number[:4])
		
		elif answering_number.startswith('140'):
			area_codes.append('140')

print("The numbers called by people in Bangalore have area codes:")
for area_code in sorted(set(area_codes)):
	print(area_code)

# Part B

count = area_codes.count('080')
total = len(area_codes)
percentage = (count * 100) / total

print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(round(percentage, 2)))