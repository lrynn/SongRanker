import csv
import traceback

import bubble

class Album:
    def __init__(self, name, isSingle=False):
        self.name = name
        self.songs = []
        self.isSingle = isSingle

    def addSong(self, song):
        self.songs.append(song)

class Song:
    songIndex = 0
    def __init__(self, album):
        self.album = album
        self.rank = self.songIndex

        Song.songIndex += 1
        self.index = Song.songIndex

    def setRank(self, rank):
        self.rank = rank

album_name = [
    "Love to Peace wa Kimi no Naka",
    "Man in the Mirror",
    "What's Going On?",
    "REPORT",
    "Escaparade",
    "Traveler",
    "Editorial",
    "Mixed Nuts",
    "Rejoice"
]
single_name = [
    "50%"
]

albums = {name: Album(name) for name in album_name}
albums["50%"] = Album("50%", isSingle=True)

songs = {}

with open('asdf.csv', 'r') as file:
    content = csv.reader(file)
    for row in content:
        album = row[1]
        song = row[0]
        songs[song] = Song(album)
        albums[album].addSong(song)

songs_names = [name for name in songs]


print("=================")
print("노래 불러오기")
print("=================")

for song, value in songs.items():
    print(song, f"(index {value.index})")
    print("album:", value.album)
    print("=================")

print("노래 불러오기 완료")
print("=================")


songs_names = bubble.bubble(songs_names)


i = 0
for song in songs_names:
    i += 1
    songs[song].setRank(i)

print("=================")
print("최종 결과")
print("=================")

for song, value in songs.items():
    print(value.rank, "위")
    print(song, f"(index {value.index})")
    print("album:", value.album)
    print("=================")

print()
print("=================")

for album, value in albums.items():
    print(f"\n{album}:\n")
    for song in albums[album].songs:
        songClass = songs[song]
        print(f"{song} ( {songClass.rank} 위)")

    print()
    print("이 앨범의 평균 성적:", sum(map(lambda x: songs[x].rank, albums[album].songs)) / len(albums[album].songs), "위")
    print("=================")