#Here is the python program to convert Seconds into Days, Hours, Minutes and Seconds.
#Code - 
def convert_seconds(seconds):
    days = seconds//(24*3600)
    seconds %= (24*3600)
    hours = seconds//3600
    seconds %= 3600
    minutes = seconds//60
    seconds %= 60
    print("Days:",days,", Hours:", hours,",Minutes:", minutes,", Seconds:", seconds)
convert_seconds(97610)