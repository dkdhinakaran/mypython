#Here is the python code to find the difference between the two time.
#Code -

import datetime
curr_time = datetime.datetime.now().time() # Current Time
print(curr_time) # Around 00:10:00

dt_obj = datetime.time(8,10,20)
print(dt_obj)

# Now Calculate the difference
diff = datetime.timedelta(hours=(dt_obj.hour - curr_time.hour), minutes=(dt_obj.minute - curr_time.minute), seconds=(dt_obj.second - curr_time.second))
print(diff)
# Thanks