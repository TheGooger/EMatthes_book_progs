favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'vova': 'pascal',
    'garik': '1c',
    }
people = ['vova', 'dasha', 'edward', 'cris', 'garik', 'elena']

for p in people:
    if p in favorite_languages:
        print("Hi " + p.title() + "! Thank you!")
    else:
        print("Hello " + p.title() + ", you should leave a choise!")
