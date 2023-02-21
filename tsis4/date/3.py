from datetime import datetime

# get current datetime
current_datetime = datetime.now()

# drop microseconds
new_datetime = current_datetime.replace(microsecond=0)

# print the new datetime
print("Current datetime:", current_datetime)
print("New datetime:", new_datetime)
