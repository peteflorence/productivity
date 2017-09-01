from __future__ import print_function
import os
import time
import sys

def beginThing(thing):
  os.system("say Now begin ... ")
  os.system("say " + thing)
  print("Currently doing: " + thing)

def minutesToSec(minutes):
  return minutes*60

interval_minutes = 15
interval = minutesToSec(interval_minutes)

def timeAndPrint(interval):
  for i in range(int(interval)):
    seconds_remaining = interval - i
    minutes_remaining = seconds_remaining / 60
    seconds_remainder = seconds_remaining % 60
    time.sleep(1)
    sys.stdout.write('\r' + str(minutes_remaining).zfill(2) + ':' + str(seconds_remainder).zfill(2) +' ' * 20)
    sys.stdout.flush() # important
  sys.stdout.write('\r' + ' ' * 20)
  print()

beginThing("Think about PhD")
timeAndPrint(interval)
beginThing("Read latest research")
timeAndPrint(interval)
beginThing("Read latest tech / business")
timeAndPrint(interval)
beginThing("Reed software blog")
timeAndPrint(interval)
beginThing("Improve this system")
timeAndPrint(interval)
beginThing("Run")
