
import json
import os.path
import copy

""" 
    Loads and holds the configuration of various domains of the game.
    Basic pattern:
        All external access to a set of configuration values are held within an IxxxConfig class.
        The IxxxConfig class is subclassed by a loader and a retriver class.
        The loader initializes super() and gets stashed in a known location by the loader creator.
        The retriver returns the loader from that location.
        All access to the data is implemented within the conmon IxxxConfig.
        The retriver caller does not know/care that it's actually accessing via a loader class.
        The magic here is __new__ of the retriver returning a different class, the preexisting loader.
        All further initialization of a class is bypassed when __new__ returns a different class.

    Notes:
        To avoid excessive validation code it is presumed that configurations and code are stable.
        This assumes careful testing when making changes to implemention, either config or code.
        Tests\GameConfigDriver.py can be used/modified for this purpose.
        Note that by default the Ixxx class might be holding raw input data which is mutable.
        The ability of a caller to unexpectly modify the raw data via retrived data requires testing.
"""

_cfgQualities = None 
_cfgGamemap = None
_cfgGlobals = None

class GameConfigLoader():
    """
    GameConfigLoader 
        loads in the game configuration from the specified json file
        creates and stores the various comfiguration domains into the associated module globals
    Only method meant to be called externally is load_game_config
    """
    def __init__(self):
        pass

    @staticmethod
    def _make_load_path( env_name, cfg_path, cfg_file ):
        """
        Creates the load source filename from passed in parameters.
        Internal class method, not expecting self.
        Static to facilitate unit testing
        """
        delim = r'\\'
        pathname = cfg_path + delim + env_name + delim + cfg_file
        return os.path.normpath(pathname)


    def load_game_config( self, env_name='Genesis', cfg_path='Config', cfg_file='GameSettings.json'):
        """ 
        Top level function to loads the game environment.

        Lower level comfiguration of the game environment. 
        Not responsible for restoration of a prior saved game state.
        Assumes configuration file preexisting under cfg_path/env_name/cfg_file.
        Relative to current working directory by default.

        Parameters: 
        env_name ['default']: (string) Name of the environment (i.e. game definitions) to load. Default: 'default'
        cfg_path ['Config']: (string) path to the env_name directory. Default: ;
        cfg_file ['GameSettings.json']: (string) Name of file holding the configuration

        Returns: boolean (for now)
        Exceptions: JSONDecodeError and tbd (for now)

        """

        self._source_filename = GameConfigLoader._make_load_path( env_name, cfg_path, cfg_file );
        if not os.path.isfile( self._source_filename ):
            print( f'{self._source_filename} does not exist' )
            return False

        rv = False
        with open( self._source_filename, 'r' ) as fp:
            try: 
                self._cfg_data = json.load( fp )
                rv = True
            except JSONDecodeError(msg,doc,pos):
                print('An error occurred in doc: msg')
                raise JSONDecodeError(msg,poc,pos)
            except OSError(errno, strerror):
                print( f'OSError exception caught, {errno}, {strerror}' )
                raise OSError(errno, strerror)
            except:
                print('Unknown exception caught, probably in open')

        self._organize( self._cfg_data )
        return rv

    def _organize( self, data ):
        """ 
        Partition/Decode the loaded data into configuration domains
        Assumed a "private method" where data will be the self._cfg_data unless called from unit test code
        """
        global _cfgQualities
        _cfgQualities = GameConfigCreate(data)
        global _cfgGamemap 
        _cfgGamemap = GameMapConfigCreate(data['game_map'])

#********************** GameConfig (Qualities) classes
class IGameConfig():
    """ 
    GameConfig provides the interface to the attributes of 'game_object' thingies
    """
    # __init__ should only get invoked by GameConfigCreate
    def __init__(self, data):
        self._cfg_data = data

    def _test_expectedkeys(self):
    # XXX next pass, pending completion of refactoring
        pass

    def get_suits(self):
        """ Returns list of available suits """
        return list( self._cfg_data['suit_attrs'].keys() )

    def get_suit_descriptor(self, suit):
        """ Returns a copy of the desciptors of a 'suit' """
        return self._cfg_data['suit_attrs'][suit]['descriptors'].copy()

class GameConfigCreate(IGameConfig):
    """ Initializes an IGameConfig from the passed in hash. """
    def __init__(self, data):
        super().__init__(data)

class GameConfig(IGameConfig):
    """ returns a previously initialized IGameConfig held in a module global """
    """ Note: the object returned by new is deliberately a different class from GameConfig """
    def __new__(cls, *args ):
        global _cfgQualities 
        # don't really need the if/else, just making it explicit that None is a possible return value
        return _cfgQualities if (_cfgQualities) else None

    def __init__(self, something):
        # 'something' is to cause a missing parameter exception if it get's here, which it shouldn't 
        pass

#***************** GameMap Config classes ****************
class IGameMapConfig():
    """ 
    (Not sure where these comments belong yet but probably not here.)
    Work in progress. 
    1.) 
    The dimisions of a game map are currently defined by a bounds array of ints or Nones.
    The length of the bounds array sets the number of diminsions.
    (Underlying implementaion supports only 2 diminsional maps at this point.)
    The value of a diminsion sets the maximum movement for that diminsion.
    None for unbounded, otherwise interpreted as a range -(bounds)/2 .. bound/2.
    This sets the center of the map at [0,0] for the convenience of placing objects on the map.
    It is possible to specify an origin of the map, so that [0,0] would become some offset from the center.
    E.g. origin[ -10, x ] with a bounds of [10000,x] would allow 5010 movements 'west' and 4990 movements 'east' from [0,0]
    In hindsight this is of questionably utility but since already implemented will be kept in case a use arises.
    2.)
    Pending definition/implementation is specification of attributes within specified locations. It is likely these features
    can feature submaps. I.e. locations within the toplevel map could hold embedded maps.
    
    """
    # __init__ should only get invoked by GameMapConfigCreate
    def __init__(self, data):
        self._cfg_data = data
        self._validate()

    def _validate(self):
        origin = self._cfg_data.get('origin')
        if ( origin == None ):
            self._cfg_data['origin'] =  [0] * self.dimisions()

    @property
    def raw_data(self):
        """ if something wants the raw data insure it's an immutable copy. Should be test code only in general """
        return copy.deepcopy(self._cfg_data)
    
    @property
    def _mutable_raw_data(self):
        """ return a mutable copy of the raw data, only use should for unit test code to tweak parameters """
        return self._cfg_data

    @property 
    def diminisions(self):
        return len(self._cfg_data['bounds'])

    @property 
    def origin(self):
        return self._cfg_data['origin'].copy();

    @property
    def lengths(self):
        return self._cfg_data['bounds'].copy()

    @property 
    def min_max_x(self):
        xmins = self._dim_min_max(self._cfg_data['bounds'][0], self._cfg_data['origin'][0])
        return xmins

    @property 
    def min_max_y(self):
        return self._dim_min_max(self._cfg_data['bounds'][1], self._cfg_data['origin'][1])

    def _dim_min_max(self, rawsize, startpoint):
        if (rawsize == None): return [None, None]
        split = int(rawsize/2) 
        #if (startpoint < split): 
        return [-split+startpoint,split+startpoint]
        #if (startpoint == 0): return [-rawsize, rawsize]
        return [-rawsize+startpoint, rawsize+startpoint]

class GameMapConfigCreate(IGameMapConfig):
    """ Initializes an IGameMapConfig from the passed in hash. """
    def __init__(self, data):
        super().__init__(data)

class GameMapConfig(IGameConfig):
    """ returns a previously initialized IGameMapConfig held in a module global """
    def __new__(cls, *args ):
        global _cfgGamemap 
        # don't really need the if/else, just making it explicit that None is a possible return value
        return _cfgGamemap if (_cfgGamemap) else None

    def __init__(self, something):
        # something is to cause a missing parameter exception if it get's here, which it shouldn't 
        pass

#***************** Globals Config classes (via cmdline args not sjon****************
class IGlobalsCfg():
    def __init__(self,args):
        self._args = args

    @property
    def player_name( self, default="" ):
        return self._get_arg_val('player_name', default)

    @property
    def dev_mode(self,default=0):
        return self._get_arg_val("dev_mode", default)

    def _get_arg_val( self, key, default ):
        return self._args[key] if key in self._args else default

class GlobalsConfigLoader(IGlobalsCfg):
    # note: use to expect argparse.Namespace, now requires caller converts to dict via vars()
    def __init__(self,args):
        super().__init__(args)
        global _cfgGlobals
        _cfgGlobals = self

class GlobalsConfig(IGlobalsCfg):
    def __new__(cls, *args ):
        global _cfgGlobals
        # don't really need the if/else, just making it explicit that None is a possible return value
        return _cfgGlobals if (_cfgGlobals) else None

    def __init__(self, something):
        # 'something' is to cause a missing parameter exception if it get's here, which it shouldn't 
        pass


