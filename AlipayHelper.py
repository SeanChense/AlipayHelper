
# coding: utf-8
# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time
import random

# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

w = 1080
h = 1780

print('go')
while True:
    time.sleep(0.4)
    wi = random.randint(0, w)
    hi = random.randint(40,h)
    print (wi + hi)
    device.touch(wi, hi, MonkeyDevice.DOWN_AND_UP)