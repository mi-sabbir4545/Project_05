import re
pattern = r"[a-z]"

if re.match(pattern, "ggghhh"):
    print("Matched")