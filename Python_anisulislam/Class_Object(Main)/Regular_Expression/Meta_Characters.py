import re
# pattern = r"^colo..r$"
pattern = r"a*"

if re.match(pattern,"coloubar"):
    print("Matched")