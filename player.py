class Player():
    def __init__(self):
        self._location = [0, 0]

    @property
    def location(self):
        return self._location       

    @location.setter
    def location(self, new_location):
        self._location = new_location
