import time
from Sqliteveritabanı.SongProject.Db_connect_and_operations import *

print("""
*************************************
WELCOME TO SONG LIST PROJECT

1.List song

2.Add new song

3.Delete song

4.Update artist

5.Check song times
*************************************

""")

song_db = Database()

while True:
    action = input("Please select action")

    if action == "q":
        print("Good Bye :)")
        song_db.close_connect()
        break

    elif action == "1":
        print("Please wait...")
        time.sleep(2)
        print("SONGS YOU HAVE IN YOUR LIST")
        song_db.list_song()

    elif action == "2":
        name = input("Name:")
        artist = input("Artist:")
        album = input("Album:")
        company = input("Company:")
        song_time = int(input("Song Time:"))

        new_song = Song(name, artist, album, company, song_time)
        print("Please wait...")
        time.sleep(2)
        song_db.add_new_song(new_song)
        print("Operation done :)")

    elif action == "3":
        are_u_sure = input("Are you sure ?")
        if are_u_sure == "Yes":
            song_name = input("Name:")
            print("Please wait...")
            time.sleep(2)
            song_db.delete_song(song_name)
            print("Operation done")

    elif action == "4":
        artist = input("New Artist:")
        old_artist = input("Old Artist:")
        song_db.update_song(artist, old_artist)
        print("Please wait...")
        time.sleep(2)
        print("Operation done :)")

    elif action == "5":
        print("Please wait...")
        time.sleep(2)
        song_db.list_song_times()

    else:
        print("Invalid action !!!")
