import time

currentTime = time.time() # get the current time

totalSeconds = int(currentTime) # get the total seconds

currentSecond = totalSeconds % 60 # get the current second

totalMinutes = totalSeconds // 60 # get the total minutes

currentMinute = totalMinutes % 60 # get the current minute

totalHours = totalMinutes // 60 # get the total hours

currentHour = totalHours % 24 # get the current hour

print(f'Current time is {currentHour:02}:{currentMinute:02}:{currentSecond:02} GMT') #:02 is a format specifier that will print the number with 2 digits, if the number is less than 2 digits it will add a 0 in front of the number

print(time.ctime())
