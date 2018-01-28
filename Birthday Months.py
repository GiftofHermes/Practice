#In this exercise, load scientist birthday JSON file from disk,
#  extract the months of all the birthdays,
# and count how many scientists have a birthday in each month.

import json
from collections import Counter

with open('Writings/info.json', 'r') as f:
    info = json.load(f)

months = dict()
for key in info:
    months[key] = info[key].replace(',', '/').split('/')[1]

months.values()
mount_count = Counter(months.values())
print('Month | Count')
for key in mount_count:
    print(key,'   |', mount_count[key])