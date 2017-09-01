from __future__ import print_function
import os
import time
import sys
from random import shuffle

# TODO
# Work in workouts in between
# Text alerts with Twilio?
# Consider browser extension?

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

def printSuggestions(list_things):
  for i in list_things:
    print(i)

workouts = ['pushups', 'judo pushups', 'leg raises', 'Y squats', 'stretch']
shuffle(workouts) 
workout_counter = 0
def provideWorkout(seconds):
  global workout_counter
  workout = workouts[workout_counter]
  workout_counter += 1
  print("say WORKOUT: " + workout)
  os.system("say WORKOUT: " + workout)
  timeAndPrint(seconds)

beginThing("Think about PhD")
printSuggestions(['Write on piece of paper...'])
timeAndPrint(interval)
provideWorkout(60)

beginThing("Read latest research")
printSuggestions(['arXiv sanity...', 'maybe also go through conference proceedings'])
timeAndPrint(interval)
provideWorkout(60)

beginThing("Read latest tech / business")
printSuggestions(['ieee spectrum', 'techrunch', 'nytimes bits blog'])
timeAndPrint(interval)
provideWorkout(60)

beginThing("Reed software blog")
printSuggestions(['joel on software', 'martin fowler', 'karpathy'])
timeAndPrint(interval)
provideWorkout(60)

beginThing("Improve this system")
printSuggestions(['write on piece of paper', 'implement'])
timeAndPrint(interval)
provideWorkout(60)

beginThing("Run")
timeAndPrint(interval)
os.system("say done!")