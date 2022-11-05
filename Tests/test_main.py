
import sys

import unittest
from playertest import PlayerTest

class TestMethods(unittest.TestCase):

    def test_player(self):
        testee = PlayerTest()
        testee.test(self)


if __name__ == '__main__':
    sys.path.append( ".." )
    unittest.main()





