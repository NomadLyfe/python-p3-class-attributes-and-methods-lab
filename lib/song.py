class Song:
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song(self)
    
    @classmethod
    def add_song(cls, song):
        cls.count += 1
        cls.artists.append(song.artist)
        cls.genres.append(song.genre)
        cls.genre_count[f'{song.genre}'] = len([genre for genre in cls.genres if genre == song.genre])
        cls.artist_count[f'{song.artist}'] = len([artist for artist in cls.artists if artist == song.artist])
