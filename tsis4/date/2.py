from datetime import datetime, timedelta

# get today's date
today = datetime.now().date()

# get yesterday's date
yesterday = today - timedelta(days=1)

# get tomorrow's date
tomorrow = today + timedelta(days=1)

# print the dates
print("Yesterday's date:", yesterday)
print("Today's date:", today)
print("Tomorrow's date:", tomorrow)
