
import sys
sys.path.append('..')

from comm_channel import SegregatedOutput
from time import sleep

print("Starting output channel")
SegregatedOutput().startup()
SegregatedOutput.get().send_message("First message")
for i in range(1,10):
    SegregatedOutput.get().send_message(f"Message {i}")
    sleep(1)


