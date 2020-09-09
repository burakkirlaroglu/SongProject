class Song():

    def __init__(self,name, artist, album, company, song_time):
        self.name = name
        self.artist = artist
        self.album = album
        self.company = company
        self.song_time = song_time

    def __str__(self):
        return f"NAME:{self.name}\nARTIST:{self.artist}\nALBUM:{self.album}\nCOMPANY:{self.company}\nSONG TIME:{self.song_time}"

