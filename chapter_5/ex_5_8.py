users = ['vova', 'dasha', 'bill', 'admin', 'siri']

for user in users:
    if user == 'admin':
        print("Hello, " + user.title() + "! Do you want to see report screeen?")
    else:
        print("Hello there " + user.title() + ", welcome back!")
