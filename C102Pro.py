import time
remind = input("What shall I remind you about?" )
print("In how many minutes?(write minutes in point for example 1min = 0.1)")
local_time = float(input())
local_time = local_time * 60
time.sleep(local_time)
print(remind)