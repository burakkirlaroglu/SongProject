create_new_table = "CREATE TABLE IF NOT EXISTS Song(name TEXT, artist TEXT, album TEXT, company TEXT, song_time INT)"

list_song_query = "SELECT * FROM Song"

insert_new_song_query = "INSERT INTO Song VALUES (?,?,?,?,?)"

delete_song_query = "DELETE FROM Song WHERE name = ?"

find_artist = "SELECT * FROM Song WHERE artist = ?"

update_song_query = "UPDATE Song SET artist = ? WHERE artist = ?"

list_song_times_query = "SELECT song_time FROM Song"