"""
    DAY-15 GREETING SIR BASED ON TIME PROBLEM SOLUN
"""

import time
t = time.strftime('%H:%M:%S')
print(t)

hour = int(time.strftime('%H'))
#print(hour)

# Greeting logic based on 24-hour format (0 to 23)
if 0 <= hour < 12:
    print("Good Morning Sir!")
elif 12 <= hour < 17:
    print("Good Afternoon Sir!")
elif 17 <= hour < 22:
    print("Good Evening Sir!")
else:
    print("Good Night Sir!")