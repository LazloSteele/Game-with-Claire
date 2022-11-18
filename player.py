class Player():
    def __init__(self, name):
        self._name = name
        self._location = [0, 0]

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location       

    @location.setter
    def location(self, new_location):
        self._location = new_location
