users = ['vova', 'dasha', 'bill', 'admin', 'siri']

if users:
    for user in users:
        if user == 'admin':
            print("Hello, " + user.title() + "! Do you want to see report screeen?")
        else:
            print("Hello there " + user.title() + ", welcome back!")
else:
    print('We need to find some users!')
