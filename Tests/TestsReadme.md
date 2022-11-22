
# Tests -- Quick notes

### Finding the modules to test
* Test code in general live in (and execute from) the projects Test subdir 
* Therefore each file should contain the following code snippet at the top
import sys
if '..' not in sys.path:
    sys.path.append( ".." )

### Unit Tests
* just learning the python unittest framework, approach may change at some point
* test_main.py is the main unit test entry
* unit testing code should be in xxxtest.py files
* a peak at test_main.py and one or two xxxtest.py files should get you started

### Interactive Testers
* files named xxxdriver.py are assumed interactive testers
* use cases
  * new modules, unstable code
  * complex model/features dev, e.g. procgen 
  * ut would be high maintenance, e.g. config changes breaking game_config tests

