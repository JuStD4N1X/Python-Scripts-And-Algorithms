class mySounds:
    def __init__(self):
        self.artist = ""
        self.album = ""
        self.songsNumber = 0
        self.year = 0
        self.downloadNumber = 0

def loadData(fileName):
    album_collection = []

    with open(fileName, 'r', encoding="utf-8") as file:
        lines = file.readlines()

        for i in range(0,len(lines),6):
            new_album = mySounds()
            new_album.artist = lines[i].strip()
            new_album.album = lines[i+1].strip()
            new_album.songsNumber = int(lines[i+2].strip())
            new_album.year = int(lines[i+3].strip())
            new_album.downloadNumber = int(lines[i+4].strip())
            album_collection.append(new_album)
    return album_collection


def dataShow(albumCollection):
    for album in albumCollection:
        print(album.artist)
        print(album.album)
        print(album.songsNumber)
        print(album.year)
        print(album.downloadNumber)
        print()

if __name__ == '__main__':
    print("Uruchamianie programu...")
    obj = mySounds()
    albums = loadData('Data.txt')
    dataShow(albums)

