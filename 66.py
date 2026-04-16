import re

vowels = "aeiou"
consonants = "qwrtypsdfghjklzxcvbnm"

pattern = r'(?<=[%s])([%s]{2,})(?=[%s])' % (consonants, vowels, consonants)
match = re.findall(pattern, input(), re.IGNORECASE)

if match:
    print(*match, sep='\n')
else:
    print(-1)
