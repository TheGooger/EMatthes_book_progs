rivers = {
    'nile': 'egypt',
    'niva': 'russia',
    'amazon':'usa',
    }

for r, c in rivers.items():
    if r == 'amazon':
        print("The " + r.title() + " runs through " + c.upper() + ".")
    else:
        print("The " + r.title() + " runs through " + c.title() + ".")

print("\nHere is the list of rivers:")
for r in rivers:
    print(r.title())

print("\nHere is the list of countries:")
for c in rivers.values():
    if c != 'usa':
        print(c.title())
    else:
        print(c.upper())
