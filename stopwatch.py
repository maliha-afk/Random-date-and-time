import time
import datetime
T= int(input("enter time in second: "))
for i in range(T):
    print(datetime.datetime.now().time())
    time.sleep(1)