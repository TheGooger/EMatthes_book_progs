def show_magicians(magicians_list):
    for magician in magicians_list:
        print(magician.title())


def make_great(magicians_list):
    k = len(magicians_list)
    for i in range(0,k):
        magicians_list[i] = "great " + magicians_list[i]
    

magicians = ['david', 'martin', 'isaak', 'robert']

show_magicians(magicians)
make_great(magicians)
show_magicians(magicians)

