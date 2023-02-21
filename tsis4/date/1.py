from datetime import datetime, timedelta

# get current date
current_date = datetime.now()

# subtract five days
new_date = current_date - timedelta(days=5)

# print the new date
print("Current date:", current_date)
print("New date:", new_date)