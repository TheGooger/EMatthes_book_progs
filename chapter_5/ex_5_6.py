age = 100

if age < 2:
    t = 'mladenec'
elif age < 4:
    t = 'malish'
elif age < 13:
    t = 'rebenok'
elif age < 20:
    t = 'podrostok'
elif age < 65:
    t = 'vzrosly'
else:
    t = 'old man'
print("You are: " + t)
