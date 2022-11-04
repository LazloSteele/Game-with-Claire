class DescribeRoom():
    def __init__(self, room):
        
        self._room = room

    @property
    def room(self):
        return self._room
        
    def look(self):
        return f"You stand before a {self.room.focus.adjective()} {self.room.focus.name}!\n"

    def enter(self):
        return f"You enter this space, it contains a {self.room.focus.adjective()} {self.room.focus.name}"

    
