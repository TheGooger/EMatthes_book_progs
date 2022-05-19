def make_album(artist_name, album_name, num_of_tracks=''):
    album = {'artist': artist_name.title(), 'album': album_name.title()}
    if num_of_tracks:
        album['number'] = num_of_tracks
    return album


print(make_album('rakim', 'speed'))
album = make_album('gosha', 'dacha', 27)
print(album)
