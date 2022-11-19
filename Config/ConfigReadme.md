
# Game configuration notes

### Testing and/or pretty printing a json file from the commandline
* python -m json.tool [filename]

## Game attribute configuration
* At present most game configuration is assumed to be living in json files
* By default the game will look for configs under .\Config\\[gamename] for fixed json file names.
  * The configuration directory and game name subdirectory can be overridden on the command line [--help for details]
  * An additional command line option is present for overriding the assumed json file name [GameConfig.json].
  * At the point where additional cfg files are introduce this option will change to be a json file name which can list specific file overloads. 
    * NOTE: This is specially a dev feature for testing alternate versions. Not meant to be used in general.

## Json files
* Versioning
  * All json config files should contain a "version" : [Major Number, Minor Number] entry with Major starting at 1, minor at 0
  * The version is unique to each specific configuration file, i.e. version numbers do not move in unison.
  * Until the code base settles down the following can be mostly ignored
    * Major number should be bumped and minor reset to 0 on breaking changes
    * Minor number should be bumpped in the case interesting non-breaking change. 
      * For changes not dependant on thebumpped the version number should be referenced in the commit tag for the associated config commit.

* Specifics of each json files pending until needed
