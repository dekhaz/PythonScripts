import time
import datetime
from datetime import datetime, timedelta


portland_time = datetime.now()
portland_time_string = portland_time.strftime('%Y-%m-%d %H:%M:%S')

##new york is +3 hours from portland
##london is +8 hours from portland

new_york_time = datetime.now() + timedelta(hours=3)
new_york_time_string = new_york_time.strftime('%Y-%m-%d %H:%M:%S')
london_time = datetime.now() + timedelta(hours=8)
london_time_string = london_time.strftime('%Y-%m-%d %H:%M:%S')



print(portland_time)
print(portland_time_string)
print(new_york_time)
print(new_york_time_string)
print(london_time)
print(london_time_string)

print ("Time in portland: " + str(portland_time.hour) + ":" + str(portland_time.minute))
if (portland_time.hour < 21 and portland_time.hour >= 9):
    print ("The store is open in portland")
else:
    print ("The store is closed in new york.")
print ("Time in new york: " + str(new_york_time.hour) + ":" + str(new_york_time.minute))
if (new_york_time.hour < 21 and new_york_time.hour >= 9):
    print ("The store is open in new york")
else:
    print ("The store is closed in new york.")
print ("Time in london: " + str(london_time.hour) + ":" + str(london_time.minute))
if (london_time.hour < 21 and london_time.hour >= 9):
    print ("The store is open in london")
else:
    print ("The store is closed in london.")




