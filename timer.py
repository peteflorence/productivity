from __future__ import print_function
import os
import time
import sys
from random import shuffle
import yaml

# TODO
# Work in workouts in between
# Text alerts with Twilio?
# Consider browser extension?

def minutesToSec(minutes):
  return minutes*60

total_minutes_available = 15
interval_minutes = total_minutes_available / 6
# interval_minutes = 15

interval = minutesToSec(interval_minutes)

def printSuggestionsFor(thing):
  if isinstance(i, dict):
    for key, value in thing.iteritems():
      for k2, v2 in value.iteritems():
        if k2 =="suggestions":
          for j in v2:
            print('- '+j)

def getThing(thing):
  if isinstance(thing, dict):
    for key, value in thing.iteritems():
      return key
  return thing

def beginThing(thing):
  os.system("say Now begin ... ")
  os.system("say " + thing)
  print("Currently doing: " + thing)

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
  workout_counter = workout_counter % len(workouts)
  print("say WORKOUT: " + workout)
  os.system("say WORKOUT: " + workout)
  timeAndPrint(seconds)


with open('things.yaml', 'r') as f:
    doc = yaml.load(f)

for i in doc:
  thing = getThing(i)
  beginThing(thing)
  printSuggestionsFor(i)
  timeAndPrint(interval)
  provideWorkout(60)

os.system("say done!")