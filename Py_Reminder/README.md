# Reminder (v0.1)

_pronounced "Reminder"_

This application is used to remind workers that when they concentrate on their work, 
it is often easy to ignore the activity required for a long time to sit down, 
so this focuses on:
1. Remind you to get up at the hour and half an hour (red window, and text reminder)
2. Remind you to sign in at the end of the day, you can customize the end of the day


## Environment
system(current) :
 - windows 10

pip library :
 - PyQt5              5.15.9

## file

    Reminder.py      code file
    1.png            app icon
    build            exe build file
    dist             exe
    Reminder.spec    build file spec

## py 2 exe
cd path cmd
Pyinstaller -F -w -i logo.png Reminder.py

