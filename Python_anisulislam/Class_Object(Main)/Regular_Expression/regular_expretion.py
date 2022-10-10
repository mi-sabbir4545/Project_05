# match function

'''import re
pattern = r"Red"
if re.match(pattern,"Red is a colour"):
    print("Match")
else:
    print("Not Matched")'''

# search function
import re
pattern = r"colour"
if re.search(pattern,"Red is a colour"):
    print("Match")
else:
    print("Not Matched")

# findall
import re
pattern = r"colour"
print(re.findall(pattern,"Red is a colour, I love red colour"))