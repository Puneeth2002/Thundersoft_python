import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

#Replace the first 2 occurrences:
