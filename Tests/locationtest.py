
import sys
if '..' not in sys.path:
    sys.path.append( '..' )

from location import LocType
from location import LocBounds
from location import Location
from location import Location_2D


class LocationTests():
    def __init__(self):
        pass

    def test(self, tester):
        boundsTest = LocBounds_T1()
        boundsTest.test(tester)
        boundsTest = LocBounds_T2()
        boundsTest.test(tester)
        boundsTest = LocBounds_T3()
        boundsTest.test(tester)

        locationTest = Location_2D_T1()
        locationTest.test(tester)


class LocBounds_T1():
    """ Tests default construction.. Everything in range """
    def __init__(self):
        self._locBounds = LocBounds()

    def test(self, tester ):
        tester.assertEqual( self._locBounds.low_in_range(0), True )
        tester.assertEqual( self._locBounds.high_in_range(0), True )
        tester.assertEqual( self._locBounds.low_in_range(-1000000000), True )
        tester.assertEqual( self._locBounds.high_in_range(1000000000), True )
        tester.assertEqual( self._locBounds.in_range(-1000000000), True )
        tester.assertEqual( self._locBounds.in_range(1000000000), True )

class LocBounds_T2():
    """ Test non-default cnstr """
    def __init__(self):
        self._high = 1000
        self._low = -self._high
        self._locBounds = LocBounds(self._low,self._high)

    def test(self, tester ):
        tester.assertEqual(self._locBounds.low_edge, self._low)
        tester.assertEqual(self._locBounds.high_edge, self._high)
        tester.assertEqual(self._locBounds.low_in_range(self._low), True )
        tester.assertEqual(self._locBounds.low_in_range(self._low-1), False )
        tester.assertEqual( self._locBounds.high_in_range(self._high), True )
        tester.assertEqual( self._locBounds.high_in_range(self._high+1), False )

class LocBounds_T3():
    """ Test setters/getters """
    def __init__(self):
        self._high = 1000
        self._low = -self._high
        self._locBounds = LocBounds(self._low,self._high)

    def test(self, tester):
        new_low = self._low*2
        self._locBounds.low_edge = new_low 
        tester.assertEqual(self._locBounds.low_edge, new_low)
        new_high = self._high*3
        self._locBounds.high_edge = new_high 
        tester.assertEqual(self._locBounds.high_edge, new_high)

class Location_2D_T1():
    def __init__(self):
        self._location = Location_2D()
        pass

    def test(self,tester):
        tester.assertEqual(self._location.dimtype() , LocType.DIM_2 )
        tester.assertEqual(self._location.is_2D() , True)
        # test north/south movements
        tester.assertListEqual( list(self._location.move_north()), [1, True])
        tester.assertEqual( self._location._north_extent, 1 )
        tester.assertListEqual( list(self._location.move_north(2)), [3, True])
        tester.assertEqual( self._location._north_extent, 3 )
        tester.assertEqual( self._location._south_extent, 0 )
        tester.assertListEqual( list(self._location.move_south()), [2, True])
        tester.assertListEqual( list(self._location.move_south(3)), [-1, True])
        tester.assertEqual( self._location._south_extent, -1 )
        tester.assertListEqual( self._location._where, [0,-1])
        # test east/west movements
        tester.assertListEqual( list(self._location.move_east()), [1, True])
        tester.assertEqual( self._location._east_extent, 1 )
        tester.assertListEqual( list(self._location.move_east(2)), [3, True])
        tester.assertEqual( self._location._east_extent, 3 )
        # test west movements
        tester.assertEqual( self._location._west_extent, 0 )
        tester.assertListEqual( list(self._location.move_west()), [2, True])
        tester.assertEqual( self._location._west_extent, 0 )
        tester.assertListEqual( list(self._location.move_west(3)), [-1, True])
        tester.assertEqual( self._location._west_extent, -1 )
        tester.assertListEqual( self._location._where, [-1,-1])


