import time

# print(time.ctime(168638763))
# print(time.time()) # return current seconds since epoch

time_object = time.localtime()

# print(time_object)
# time_object = time.gmtime()
# time_string = time.strftime('%B %d %Y %H:%M:%S',time_object)
# print(time_string)

# parse string representation of time and/or day
# time_string = '15 May, 2022'
# time_object = time.strptime(time_string, '%d %B, %Y')
# print(time_object)

# (year, month, day, hours, min, sec, #day of the week, #day of the year, dst)
time_tuple = (2019, 5, 15, 15, 43, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)

# (year, month, day, hours, min, sec, #day of the week, #day of the year, dst)
time_tuple = (2019, 5, 15, 15, 43, 0, 0, 0, 0)
time_string = time.mktime(time_tuple)
print(time_string)