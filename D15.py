#Exercise2
'''
    Create a python programe capable of greeting you with good morning, good afternoon, or good evening.
    Your program should use time module to get the current hour.
'''

import time
current_time = time.localtime()
hour = current_time.tm_hour
if hour < 12:
    print("Good morning!")
elif hour < 18:
    print("Good afternoon!")
else:    
    print("Good evening!")