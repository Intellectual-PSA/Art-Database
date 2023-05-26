class ArtDatabase:
    def __init__(self):
        self.artworks = {}

    def add_artwork(self, title, artist, year, movement):
        self.artworks[title] = {'artist': artist, 'year': year, 'movement': movement}

    def remove_artwork(self, title):
        if title in self.artworks:
            del self.artworks[title]

    def get_artwork_details(self, title):
        return self.artworks.get(title, None)

    def list_artworks(self):
        for title, details in self.artworks.items():
            print(f"Title: {title}, Artist: {details['artist']}, Year: {details['year']}, Movement: {details['movement']}")

# Sample usage
if __name__ == "__main__":
    db = ArtDatabase()

    db.add_artwork("The Starry Night", "Vincent van Gogh", 1889, "Post-Impressionism")
    db.add_artwork("The Scream", "Edvard Munch", 1893, "Expressionism")
    db.add_artwork("The Persistence of Memory", "Salvador Dali", 1931, "Surrealism")

    db.list_artworks()

    print(db.get_artwork_details("The Starry Night"))

    db.remove_artwork("The Scream")

    db.list_artworks()
