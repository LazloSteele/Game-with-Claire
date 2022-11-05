from player import Player
from controller import Controller
from game_state import GameState

class Game():
    def __init__(self):
        self._player = Player()
        self._game_state = GameState(self._player)
    
        self._controller = Controller(self._game_state)

        self._current_room = self._game_state.current_room()

        self.main()

    def main(self):
        playing = True

        print('Type "QUIT" at any time to exit the game.')
        self._controller.look(None)
        
        while playing == True:
        
            command = input("What do you do?")

            if command.upper() == 'QUIT':
                playing == False
                return

            self._controller.interpret(command)
            
if __name__ == "__main__":
    game = Game()


