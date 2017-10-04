import webbrowser
import time

print("WELCOME TO POMODORO!! \n")

name = input("What is your name? \n")

mins = int(input("Welcome %s !\n How many minutes do you want to work?\n " % (name)))

work_session = int(input(" How many sessions of work? \n"))

Time_break = int(input(" How many minutes of break? \n"))

tmsecs = Time_break * 60

secs = mins * 60

choice =  int(input(" How would do i remind you the break time? \n Choose the number. \n 1) Play a music video for me. \n 2) Open facebook \n"))

while(work_session != 0):

  if choice == 1:

    print(time.ctime())

    print(" Done! See you after %s minutes!" %(mins) )

    time.sleep(secs)

    print(" Break Time :)  !! ")

    webbrowser.open("https://www.youtube.com/watch?v=DHITmcKUGik&index=13&list=RDMMp3kRuy-Jgqk")

    time.sleep(tmsecs)

    work_session -= 1

  elif choice == 2:

    print(time.ctime())

    print(" Done! See you after %s minutes!" %(mins))

    time.sleep(secs)

    print(" Break Time :)  !! ")

    webbrowser.open("https://www.facebook.com/")

    time.sleep(tmsecs)

    work_session -= 1

  else:

    print(" Wrong choice!")

print("Your session is Over!! Good Work")