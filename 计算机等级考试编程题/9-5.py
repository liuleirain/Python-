# 利用time库将当前日期时间转化成类似‘Sunday，8.January 2017 11:03PM’的格式。
import time

current_time = time.localtime()
print(time.strftime('%A, %d.%B %Y %I:%M%p', current_time))
