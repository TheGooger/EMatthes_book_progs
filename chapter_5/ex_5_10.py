current_users = ['vova', 'dasha', 'bill', 'george', 'siri']
new_users = ['alex', 'siri', 'carl', 'dominic', 'DASHA']

for user in new_users:
    if user.lower() in current_users:
        print("Sorry " + user + ", this name is not available! Choose another name.")
    else:
        print(user + " you can choose this name!")
