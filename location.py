
from enum import Enum,auto

class LocType(Enum):
    DIM_2 = auto()      # 2 dimisional, lexicon is n/s/e/w
    DIM_3 = auto()      # 3 dimisional, lexicon n/s/e/w/u/d
    ANYWHERE = auto()
    NOWHERE = auto()
    HIDDEN = auto()

class LocBounds():
    """
      Sets minimal and maximal limits for a value
    """
    def __init__(self, min_bound=None, max_bound=None):
        self._low_edge = min_bound
        self._high_edge = max_bound

    @property
    def low_edge(self): return self._low_edge;

    @low_edge.setter
    def low_edge(self,val): self._low_edge = val

    @property
    def high_edge(self): return self._high_edge

    @high_edge.setter
    def high_edge(self,val): self._high_edge = val

    def low_in_range(self,val):
        return self.low_edge == None or val >= self.low_edge 

    def high_in_range(self,val):
        return self.high_edge == None or val <= self.high_edge 

    def in_range(self,val):
        return self.low_in_range(val) and self.high_in_range(val)

class Location():
    def __init__(self, loc_type = LocType.NOWHERE):
        self._dimtype = loc_type

    def dimtype(self): return self._dimtype

    def is_2D(self): return False
    def is_3D(self): return False
    # anywhere/nowhere/hidden or placeholder for potential future expansion
    def is_anywhere(self): return False
    def is_nowhere(self): return False
    def is_hidden(self): return False


class Location_2D(Location):
    def __init__(self,x=0,y=0,x_min=None,x_max=None,y_min=None,y_max=None):
        super().__init__(LocType.DIM_2)
        self._where = [x,y]
        self._east_extent = self._west_extent = x
        self._north_extent = self._south_extent = y
        self._x_bounds = LocBounds(x_min, x_max)
        self._y_bounds = LocBounds(y_min, y_max)
        pass

    def is_2D(self):
        return True

    def set_eastwest(self,val):
        pass

    def set_northsouth(self,val):
        pass

    def move_north(self, steps=1):
        assert(steps > 0)
        return self._testmove_y(steps)

    def move_south(self, steps=1):
        steps = -steps if steps > 0 else steps
        return self._testmove_y(steps)

    def move_east(self, steps=1):
        assert(steps > 0)
        return self._testmove_x(steps)

    def move_west(self, steps=1):
        steps = -steps if steps > 0 else steps
        return self._testmove_x(steps)

    def _testmove_y(self, steps):
        assert(steps!=0)
        temp = self._where[1] + steps
        ok = self._y_bounds.in_range(temp)
        if (ok):
            self._where[1] = temp
            if (steps>0): 
                self._north_extent = max(self._north_extent, temp)
            else:
                self._south_extent = min(self._south_extent, temp)
        return self._where[1], ok

    def _testmove_x(self, steps):
        assert(steps!=0)
        temp = self._where[0] + steps
        ok = self._x_bounds.in_range(temp)
        if (ok):
            self._where[0] = temp
            if (steps>0): 
                self._east_extent = max(self._east_extent, temp)
            else:
                self._west_extent = min(self._west_extent, temp)
        return self._where[0], ok


