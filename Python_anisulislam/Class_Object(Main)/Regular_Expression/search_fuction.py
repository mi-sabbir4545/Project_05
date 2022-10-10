import re

pattern = r"colour"
text = "My favorite colour is Red"
match = re.search(pattern, text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())
