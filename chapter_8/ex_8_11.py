def show_magicians(magicians_list):
    for magician in magicians_list:
        print(magician.title())


#def make_great(magicians_list):
#    k = len(magicians_list)
#    for i in range(0,k):
#        magicians_list[i] = "great " + magicians_list[i]
#    return magicians_list
    
    
def make_great(magicians_list, great_magicians):
    while magicians_list:
        current_magician = magicians_list.pop()
        great_magicians.append("great " + current_magician)

magicians = ['david', 'martin', 'isaak', 'robert']
gr_mag = []

show_magicians(magicians)
make_great(magicians[:], gr_mag)
show_magicians(gr_mag)
print("\n")
show_magicians(magicians)


