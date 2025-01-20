# Write a function that returns a string in the form of hour:minute:second for a given total seconds using the following header:

# def format(seconds):

# Here is a sample run:

# <Output>
# Enter total seconds: 342324 <enter icon>

# The hours, minutes, and seconds for total seconds 342324 is 23:05:24
# <End Output>

# Note that a zero is padded to hour, minute, and second if any of these values is a single digit.
# (Limit the hours part whithin 24 hours, as shown above)

seconds = eval(input('Enter total seconds: '))
def format(seconds):
    minutes = seconds // 60
    remainingSeconds = seconds % 60
    hours = minutes // 60
    remainingMinutes = minutes % 60
    if hours > 24:
        hours = 23
    return f'The hours, minutes, and seconds for total seconds {seconds} is {hours:02}:{remainingMinutes:02}:{remainingSeconds:02}'
print(format(seconds))