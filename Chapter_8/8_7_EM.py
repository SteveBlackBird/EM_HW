# Album

def make_album(group_name, album_name, age=None):
    # albums = {'group': group_name, 'album': album_name,}
    albums = {}
    albums[group_name] = album_name
    if age:
        albums['treks'] = age
    return albums

album01 = make_album('linkin park', 'meteora')
album02 = make_album('sylar', 'sylar')
album03 = make_album('asap ferg', 'new level', age=8)
albums = [album01, album02, album03]
print(albums)