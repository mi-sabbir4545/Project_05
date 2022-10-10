# sub function
import re

pattern = r"colour"
text1 = "My favourite colour. i love colour"
text2 = re.sub(pattern, "color", text1, count=1)
print(text2)
