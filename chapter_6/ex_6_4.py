glossary = {
    'dyn_var': 'Dyn. var. is var. without "strong" type.',
    'inter': 'Interpreter is not compiler.',
    'tab': 'Tab is equal 4 spaces.',
    'tups':'tups cannot be changed',
    'lists': 'lists can be changed',
    'PEP8': 'You have to follow it!',
    }

for key, value in glossary.items():
    print("\nThe definition or interesting fact about " +
    key.title() + " is:\n\t" + value)
