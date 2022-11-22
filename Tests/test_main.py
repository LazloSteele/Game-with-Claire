
import sys
if '..' not in sys.path:
    sys.path.append( '..' )

import unittest
from playertest import PlayerTest
from locationtest import LocationTests

class TestMethods(unittest.TestCase):

    def test_player(self):
        testee = PlayerTest()
        testee.test(self)

    def test_location(self):
        testee = LocationTests()
        testee.test(self)


if __name__ == '__main__':
    unittest.main()





