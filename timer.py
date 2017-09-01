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
interval = 5

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

def printSuggestions(list_things):
  for i in list_things:
    print(i)

beginThing("Think about PhD")
printSuggestions(['Write on piece of paper...'])
timeAndPrint(interval)

beginThing("Read latest research")
printSuggestions(['arXiv sanity...', 'maybe also go through conference proceedings'])
timeAndPrint(interval)

beginThing("Read latest tech / business")
printSuggestions(['ieee spectrum', 'techrunch', 'nytimes bits blog'])
timeAndPrint(interval)

beginThing("Reed software blog")
printSuggestions(['joel on software', 'martin fowler', 'karpathy'])
timeAndPrint(interval)

beginThing("Improve this system")
printSuggestions(['write on piece of paper', 'implement'])
timeAndPrint(interval)

beginThing("Run")
timeAndPrint(interval)
os.system("say done!")