import numpy as np
import time as t
import threading
from prompt_toolkit import PromptSession
from sys import stdout as o
# import pandas as pd
# import random as r
# it's a temporary a mock file, soon i will implement it.


def r_time(loop: bool = True):
    i = 0
    while loop:
        i+=1
        
        # o.write(f"\rtime: {i}")
        # o.flush()
        # t.sleep(1)