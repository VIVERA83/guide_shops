import re

msg = "+7(981)861-43-44"

# pattern = "^((8|\+7)[\- ]?)?(\(?\d{3,4}\)?[\- ]?)?[\d\- ]{5,10}$"
pattern = "\d"
res = ''.join(re.findall(pattern, msg))
print(res)
