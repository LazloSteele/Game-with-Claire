
from time import sleep
import sys


class TerminalClient():
    def __init__(self):
        pass

    def run(self):
        print("")
        while (1):
            line = input()
            print(line)
            sleep(1)



tc = TerminalClient()
tc.run()


