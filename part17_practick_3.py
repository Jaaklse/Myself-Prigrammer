import re

text = 'Привидение прошуршало и исчезло в углу'
#text1 = text.split()
matches = re.findall('[аз]ло', text, re.IGNORECASE)
print(matches)

