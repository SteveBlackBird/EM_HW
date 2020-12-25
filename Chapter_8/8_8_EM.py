# Custom album

albums = {}
active = True

def make_album(group_name, album_name):
    """ Need redo """
    albums = {}
    albums[group_name] = album_name
    return albums

while active:
    group_name = input("group_name: ")
    album_name = input("album_name: ")
    unic_name = group_name + album_name

    album_custom = make_album(group_name, album_name)
    albums[unic_name] = album_custom
    repeat = input("Any one else? 'Y/N':")
    if repeat == 'N':
        active = False


print("_____Group albums_____")
for keys, values in albums.items():
    for key, value in values.items():
        print(f"{key.upper()} - {value.title()}")