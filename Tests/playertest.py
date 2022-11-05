
import sys
sys.path.append( ".." )

from player import Player
player = Player()

class PlayerTest():
    def __init__(self):
        pass

    def test(self, tester ):
        expected = [0,0]
        tester.assertListEqual( player.location, expected )
        expected = [1,3]
        player.location = expected
        tester.assertListEqual( player.location, expected )


