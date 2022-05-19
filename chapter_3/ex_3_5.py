visitors = ['Dasha', 'Mom', 'Granny']
print('Hello, dear ' + visitors[0] + '! I want to invite you to my dinner!')
print(visitors[1] + ' would you like to visit my dinner?')
print(visitors[2] + ' is going to be there!')
#person = visitors.pop(0)
#new_person = 'Sister'
#visitors.insert(0, new_person)
print(visitors[0] + ' cannot come to my dinner!')
visitors[0] = 'Sister'
print('New list of visitors: ' + str(visitors) + '\n')
print(visitors[1] + ' would you like to visit my dinner?')
print(visitors[2] + ' is going to be there!')
print(visitors[0] + ' will come too!')
