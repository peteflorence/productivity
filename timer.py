import os
import time

def beginThing(thing):
  os.system("say Now begin ... ")
  os.system("say " + thing)
  print("Currently doing: " + thing)

def minutesToSec(minutes):
  return minutes*60

interval_minutes = 0.1
interval = minutesToSec(interval_minutes)

beginThing("Run")
time.sleep(interval)
beginThing("Think about PhD")
time.sleep(interval)
beginThing("Read latest research")
time.sleep(interval)
beginThing("Read latest tech / business")
time.sleep(interval)
beginThing("Reed software blog")
time.sleep(interval)
beginThing("Improve this system")