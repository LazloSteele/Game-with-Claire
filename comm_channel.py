
from subprocess import Popen, PIPE, STDOUT,CREATE_NEW_CONSOLE
from time import sleep
import re

""" 
    Handles game level output which is not intended to comingle with player 
    level dialog. 
    This first pass is almost certainly backwards and should be flipped on its
    head with players having seperated channels.
    Probably (somewhat) sooner than (much) later should be looking at moving to
    a client/server model. 
"""
# singleton class for first pass
segregatedOutput=None

class SegregatedOutput():
    def __init__(self):
        self._child_proc = None
        pass

    def get(): 
        global segregatedOutput
        return segregatedOutput

    def startup(self):
        if (self._child_proc != None): self.shutdown()
        assert(self._child_proc == None)
        self._child_proc = Popen(["python","game_oracle_client.py"], shell=False, text=True, stdin=PIPE, stdout=None, stderr=None, creationflags=CREATE_NEW_CONSOLE)
        global segregatedOutput
        segregatedOutput=self

    def  _kill_child(self):
        if (self._child_proc != None):
            self._child_proc.terminate()
            for _ in range(0,5):
                if (self._child_proc.poll() == None):
                    self._child_proc.stdin.close()
                    self._child_proc = None
                    break;
                sleep(1)
            assert(self._child_proc == None)        # XXX pending error handling, just assert for now

    def shutdown(self):
        self._kill_child()
        global segregatedOutput
        segregatedOutput = None

    def child_is_alive(self):
        return self._child_proc != None and self._child_proc.poll() == None

    # XXX raw text message for first pass, protocol definition pending
    def send_message(self, message, verbose=False ):
        if self.child_is_alive():
            print(f"Sending message '{message}'")
            if re.search('\n$', message) == None:
                message += '\n';
            self._child_proc.stdin.write(message)
            self._child_proc.stdin.flush()
        elif (verbose): print(f"In send_message, with {message}")


if __name__=="__main__":
    """ quick test """ 
    SegregatedOutput().startup()
    SegregatedOutput.get().send_message("Game comm channel ...")
    i = 0
    for i in range(1, 10):
        SegregatedOutput.get().send_message(f"Message {i}",verbose=True)
        sleep(1)
    SegregatedOutput.get().shutdown()
    sleep(2)

 
