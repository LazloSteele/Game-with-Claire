# Game Objects

Work in progress. Non structured list of potential objects within the game.

#### Game
* has PlayerQueue
* has Universe
* uses PlayerInput (interpretor)
* has PlayerMode (interactive/scripted)
* has EventQueues (tbd)
* event generator ... Save, tbd
* uses random generators (dice, timers) ... Placeholder, may not belong here

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

### Universe
* has GameMap
* can receive GameMapEvents

### GameMap
* has Rooms
* has Regions ... tbd
* has Towns ... tbd


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
      
          
