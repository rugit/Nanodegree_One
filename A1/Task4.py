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
not_telemarketers = {}
telemarketers = {}

for i in texts:
	not_telemarketers[i[0]] = 1
	not_telemarketers[i[1]] = 1

for i in calls:
	not_telemarketers[i[1]] = 1

not_telemarketers_number = not_telemarketers.keys()

for i in calls:
	if(i[0] not in not_telemarketers_number):
		telemarketers[i[0]] = 1

print("These numbers could be telemarketers: \n{}".format("\n".join(sorted(telemarketers.keys()))))

