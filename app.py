from flask import *
import os
import re

VALID_FILES = [".wav", ".mp3", ".ogg", ".flac"]
SONGS_DIR = "C:/Users/raxix/Music"

class Song(object):
	def __init__(self, path):
		self.path = path.replace("'", "\\u0027")
		reg = re.findall(".:/.*/(.*)\.(.*)", path)[0]
		self.song = reg[0]
		self.ext = reg[1]

def get_songs():
	songs = []
	for root, dirs, files in os.walk(SONGS_DIR):
		for file in files:
			for ext in VALID_FILES:
				if ext in file:
					rep = '\\'
					songs.append(Song(f"{root.replace(rep, '/')}/{file}"))
	
	return songs

app = Flask(__name__)

@app.route('/')
def index():
	if request.args:
		key = request.args.get("key")
		songs = [ x for x in get_songs() if key in x.song + x.ext]
	else:
		key = ""
		songs = get_songs()
	
	return render_template("index.html", songs = songs, key = key)

if __name__ == '__main__':
	app.run()
