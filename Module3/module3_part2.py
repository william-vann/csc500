# Module 3 - Part 2 

# Get user inputs
time_now = int(input('Enter time now (0-23): '))
hours_to_alarm = int(input('Enter hours until alarm: '))

# Define 24 hour clock dictionary
clock_24hour = {
    0: (0, '12am (midnight)', 'o zero hundred'), 
    1: (1, '1am', 'o one hundred'),
    2: (2, '2am', 'o two hundred'), 
    3: (3, '3am', 'o three hundred'),
    4: (4, '4am', 'o four hundred'),
    5: (5, '5am', 'o five hundred'),
    6: (6, '6am', 'o six hundred'), 
    7: (7, '7am', 'o seven hundred'),
    8: (8, '8am', 'o eight hundred'),
    9: (9, '9am', 'o nine hundred'),
    10: (10, '10am', 'ten hundred'),
    11: (11, '11am', 'eleven hundred'),
    12: (12, '12pm (noon)', 'twelve hundred'),
    13: (13, '1pm', 'thirteen hundred'),
    14: (14, '2pm', 'fourteen hundred'),
    15: (15, '3pm', 'fifteen hundred'),
    16: (16, '4pm', 'sixteen hundred'),
    17: (17, '5pm', 'seventeen hundred'),
    18: (18, '6pm', 'eighteen hundred'),
    19: (19, '7pm', 'nineteen hundred'),
    20: (20, '8pm', 'twenty hundred'),
    21: (21, '9pm', 'twenty one hundred'),
    22: (22, '10pm', 'twenty two hundred'),
    23: (23, '11pm', 'twenty three hundred')
}

print('Current time:', clock_24hour[time_now])

# Calculate alarm time using modulo
alarm_time = clock_24hour[(time_now + hours_to_alarm) % 24]

# Display the results
print(f'Alarm will sound in {hours_to_alarm} hours')
print(f'That will be at: {alarm_time[0]} hours, aka {alarm_time[1]}, or, militarily, {alarm_time[2]}')