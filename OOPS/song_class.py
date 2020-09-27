class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


birthday_song = Song([
    "Santhosha Janma dinam kutik",
    "Heppy birthday"
])

birthday_song.sing_me_a_song()
