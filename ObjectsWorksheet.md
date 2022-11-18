# Game Objects

Work in progress. Non structured list of potential objects within the game.

## Current 
##### Game
* has a player -- attached to game_state, otherwise not accessed
* has a game_state -- attached to controller, (dangling access for current_room)
* has a current_room -- not accessed
* has a controller

##### Controller
    basically command dispatching
* has a game_state
* has a action, target -- not needed, can be locals pass directly to dispatch

##### Game_state
* has the (site) map
* has the player
* has a season

##### Room
* has name
* has content
* has focus (? player specific)

##### Player
* has location

##### Game object and multiple related modules
* documentation pending 
## End Current

****************************************************************
## Start Refactored

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

### Player
* is a PlayerCreature
* has location
* can receive PlayerEvents
* can generate PlayInputEvents

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
          
### Game objects
* have name, description
* receives game object events
* generates game object events
      
          
