  
"""Python tutor matching created for online Tutors, Brady Anderson 2020"""
# module imports
import csv
import os
import pandas as pd
import numpy as np

# global configs
"""
+================================+
  Tutor Match
  Copyright Brady Anderson, 2020
+================================+
"""
# connected our data to the tutor matching algorithm
pd.options.mode.chained_assignment = None
df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "tutorInfo.csv"))
DAYS = ["Monday", "Tuesday", "Thursday", "Friday", "Saturday", "Sunday"]
COURSES = ["I210", "I211", "I308", "C200", "C211", "C343", "C335", "I101", "I201", "C291", "B351", "C212", "C241", "E101", "E110", "E111", "I202", "I300", "M200", "M211", "M311", "M312"]
NAMES = ["Jacob", "Andrew", "Zain", "Kevin", "Shreyas", "Harshad", "Manuja", "Michael", "Jack", "Krish", "Maxwell", "Dane", "Dylan", "Cheng", "Cole", "Julie", "Taylor", "Jo", "Harrison"]

# to get the right time -> if day fits 
def findTutors(time=None, day=None, tutor=None, courses = None):
  # name provided
  if(tutor != None):
    # match for tutor name, they cover course, they are available on day 
    # with these results we will clean them to get an tutor that time matches
     q = df.loc[(df["Day"].str.contains(day, regex = False) & (df["Courses"].str.contains(courses, regex = False)) & (df["First"].str.contains(tutor, regex=False) ))]
  else:
    # no name provided -> look for day and course match time will be dealt w/ below
     q = df.loc[(df["Day"].str.contains(day, regex = False) & (df["Courses"].str.contains(courses, regex = False)))]
  # handle time works value here
  nameList = [x for x in q["First"]]
  timeList = [x for x in q["Time"]]
  dayList = [x for x in q["Day"]]
  q["inTime"] = False
  for i in range(len(nameList)):
    index = dayList[i].split(", ").index(day)
    if(time != None):
      timeStart = float(timeList[i].split(", ")[index].split("-")[0])
      timeEnd = float(timeList[i].split(", ")[index].split("-")[1][:-2])
      # when there is at least 30 mins of time available for tutoring then tutors should match
      q["inTime"][i] = True if time >= timeStart and time <= timeEnd - .5 else False
    else:
      q["inTime"] = False
  # remove values that do not match on time w/ student use : for efficency
  qb = q.loc[q["inTime"], :]
  return qb


if __name__ in "__main__":
  print(findTutors(time = 2.0, day="Monday", tutor=None, courses="C200"))