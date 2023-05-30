import csv
import os

with open("day_56_music_playlist.csv") as file:
    reader = csv.DictReader(file)
    try:
        os.mkdir("songs")
    except:
        pass

    for row in reader:
        directory = os.listdir("songs")
        artist = row["Artist(s)"].title()
        if artist not in directory:
            os.makedirs(f"songs/{artist}")
        song = row["Song"]
        path = os.path.join(f"songs/{artist}/", f"{song}")
        f = open(path, "w")
        f.close()
