# write a program that converts seconds into time

seconds = eval(input('Enter seconds: ')) # get the users seconds

minutes = seconds // 60 #finding how many minutes
remainingSeconds = seconds % 60 #finding how many seconds left after minutes
hours = minutes // 60 
remainingMinutes = minutes % 60

if hours<1 :
    print(f'You have {minutes} minute{"" if minutes == 1 else "s"} and {remainingSeconds} second{"" if remainingSeconds == 1 else "s"}')
    # print('You have ', minutes, ' minutes and ', remainingSeconds, ' seconds')
else:
    print(f'You have {hours} hours, {remainingMinutes} minutes and {remainingSeconds} second')
    print ('You have ',hours, ' hours, ', remainingMinutes, ' minutes and ', remainingSeconds, ' seconds')

