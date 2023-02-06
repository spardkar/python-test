'''
Reading CSV and cleaning the value
'''
import csv
from collections import defaultdict
from pprint import pprint

total_input = 0
total_output = 0
top_talkers = []

devices = defaultdict(list)
#file path should be exact
file_path = "/Users/satishparadkar/Documents/Ansible-REPO/PycharmProjects/pythonProject1/stats.csv"
with open(file_path, 'r') as fh:
    csv_reader = csv.DictReader(fh)

    for sw in csv_reader:

        if not sw['output'].isnumeric():
            sw['output'] = 0

        if not sw['input'].isnumeric():
            sw['input'] = 0

        if sw['device'] not in devices:
            devices[sw['device']] = [0, 0]

        if sw['device'] in devices:
            devices[sw['device']][0] = devices[sw['device']][0] + int(sw['input'])
            devices[sw['device']][1] = devices[sw['device']][1] + int(sw['output'])

        top_talkers.append(sw)

print('Top talkers devices based on input traffic:')
pprint(sorted(top_talkers, key=lambda x: int(x['input']), reverse=False))
# prints traffic what it has devices dictionary 
print('\n', 'Total traffic per device:')
for device, traffic in devices.items():
    print(device, traffic)
    print(f'Total traffic on {device} is {traffic[0] + traffic[1]}')
