import re

thousand = 'M{0,3}'
hundred = '(CM|CD|D?C{0,3})'
ten = '(XC|XL|L?X{0,3})'
digit = '(IX|IV|V?I{0,3})'

regex_pattern = r"^" + thousand + hundred + ten + digit + r"$"



