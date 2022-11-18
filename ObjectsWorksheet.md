# Game Objects

Work in progress. 

### Game
No properties
Responsible for 
* processing cmd line parameters
* loading game config
* instantiating game_impl and passing control

### game_impl -- abstract game class
* run method

### GenesisGame -- initial game impl
* has a GameState
* has a Controller
in process, moving controller into actors
    
### Controller
currently
* has an attached game_state
* handles the player action
in process, subclassing for various active components .. initially player


### GameState
currently
* has the (site) map (raw hash, which it maintains)
* has a human player
* has a season
* has a current_room concept 
projected 
* has a sitemap object 
* has a player list
* current_room is held within the players context

##### Player    
* has location (raw array with a getter/setter)
inprocess
* (consider inheriting from 'Actor' abstraction) 
* has Controller()
* inherits from PlayerContext
* subclassed by HumanPlayer
projected
* location will be held within a tbd.Location() object, 
* -- to be flushed out --


##### GameObject and related GameAssets related modules
* documentation pending 

*Below here are varying levels or correctness, randomness, and just plain wrong*

##### Room
* has name
* has content
* has focus (? player specific)

#### Game
* has PlayerQueue
* has GameMaze
* uses PlayerInput (interpretor)
* has PlayerMode (interactive/scripted)
* has EventQueues (tbd)
* event generator ... Save, tbd
* uses random generators (dice, timers) ... Placeholder, may not belong here
* has cycles

### Cycles
* has (is?) a cycle queue
* receives CycleQueueEvent
* generates CycleEvents

### PlayerQueue
* has Players
* has state: activePlayer
* generates PlayerEvent
* receives PlayerQueueEvent

### GameOutput
* receives GameOutputEvents
* generates GameOutputResponse

### PlayerInput
* has input state
* has input history (need use case)
* has input method
* has input interpretor
* sources PlayerQueueEvent(PlayerEvent)
* receives PlayerInputEvent

### Player Generator
* has build mode .. automated/interactive
* can load
* can save

### PlayerCreature
* has name
* has description
* has control type (interactive/ai)
* has divinity status
* has location
* has skills
* can generate events (tbd)
* can receive events (tbd
* have Event state
   * Event state
    * active -- receive active events
    * passive – receive background events
    * inactive – receives no events 
* has health
* can have impairment
* can have enhancements
* has dispositions
* has PlayerObjects

### GameMaze
* can receive GameMapEvents
* has Rooms
* can have Regions 
* can have Towns 
* can have geographic features

### Room
* has location
* has RoomBounderies
* has RoomInternal

### RoomBounderies
* has location (enum north/south/east/west/over/under)
* has RoomDoor(s)

### RoomDoor
* RoomBoundaryLocation
* LockedState
* Visible
          
          
