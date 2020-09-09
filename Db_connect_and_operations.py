import sqlite3
from Sqliteveritabanı.SongProject.Query import *
from Sqliteveritabanı.SongProject.Song import *
class Database():

    def __init__(self):

        self.connect()

    def connect(self):
        try:
            self.con = sqlite3.connect("SongDb.db")
            self.cursor = self.con.cursor()

            self.cursor.execute(create_new_table)
            self.con.commit()
        except ConnectionError:
            print("Connection or Table exists error.")
    def close_connect(self):
        try:
            self.con.close()
        except:
            print("Connection is not closing")
    def list_song(self):
        try:
            self.cursor.execute(list_song_query)
            all_song = self.cursor.fetchall()

            if len(all_song) == 0:
                print("There is no song !!!")
            else:
                for s in all_song:
                    song = Song(s[0], s[1], s[2], s[3], s[4])
                    print(song)
        except ConnectionError:
            print("Please check your connection")

    def add_new_song(self, song):
        try:
            self.cursor.execute(insert_new_song_query, (song.name, song.artist, song.album, song.company, song.song_time))
            self.con.commit()
        except ConnectionError:
            print("Please check your connection")

    def delete_song(self, name):
        try:
            self.cursor.execute(delete_song_query, (name,))
            self.con.commit()
        except:
            print("Please check your connection")

    def update_song(self, new_artist, artist):
        try:
            self.cursor.execute(find_artist, (artist,))
            artists = self.cursor.fetchall()

            if len(artists) == 0:
                print("There is no Artists")
            else:
                old = artists[0][1]
                self.cursor.execute(update_song_query,(new_artist, old))
                self.con.commit()

        except ConnectionError:
            print("Please check your connection")

    def list_song_times(self):
        try:
            total_time = 0
            self.cursor.execute(list_song_times_query)
            s_times = self.cursor.fetchall()

            if len(s_times) == 0:
                print("There is no song !!!")
            else:
                for times in s_times:
                    for time in times:
                        total_time += time
                print(total_time)
        except ConnectionError:
            print("Please check your connection")
