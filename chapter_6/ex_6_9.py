favorite_places = {
    'vova': ['home', 'hookah', 'beach'],
    'dasha': ['theater', 'restaurant'],
    'gosha': ['bar'],
    } 

for name, places in favorite_places.items():
    if len(places) == 1:
        print("\n" + name.title() + "'s favorite place is:")
    else:
        print("\n" + name.title() + "'s favorite places are:")
    for p in places:
        print("\t" + p.title())
