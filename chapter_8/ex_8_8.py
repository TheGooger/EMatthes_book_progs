def make_album(artist_name, album_name, num_of_songs=''):
    album = {'artist': artist_name.title(), 'album': album_name.title()}
    if num_of_songs:
        album['Number of songs'] = num_of_songs
    return album


while True:
    print("Enter name of artist and name of album.")
    print("You can also add number of songs. Press Enter, if you don't want to.")
    print("If you want to quit just enter 'q'.")
    artist = input("Artist name: ")
    if artist == 'q':
        break
    album = input("Album name: ")
    if album == 'q':
        break
    number = input("Number of songs: ")
    if number == 'q':
        break
    maked_album = make_album(artist, album, number)
    print(maked_album)
    

