class Navigation():
    def __init__(self, game_state):
        self._game_state = game_state
        self._room = self._game_state.current_room()
        self._exits = self._room.exits

    def is_valid(self, direction):
        if direction.upper() in self._exits:
            return True
        else:
            return False

    def travel(self, direction):
        if self.is_valid(direction):
            if direction == 'NORTH':
                self._game_state.player.location[1] += 1
            elif direction == 'SOUTH':
                self._game_state.player.location[1] -= 1
            elif direction == 'EAST':
                self._game_state.player.location[0] += 1
            elif direction == 'WEST':
                self._game_state.player.location[0] -= 1
        
            self._game_state.update_map()
                
        else:
            print("there is no exit that way...")
