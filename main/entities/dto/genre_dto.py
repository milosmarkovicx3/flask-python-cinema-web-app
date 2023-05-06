class GenreDTO:
    def __init__(self, id, name, image):
        self.id = id
        self.name = name
        self.image = image

    def __str__(self):
        return str(self.__repr__())

    def __repr__(self):
        return {
            "id": self.id,
            "name": self.name,
            "image": self.image
        }
