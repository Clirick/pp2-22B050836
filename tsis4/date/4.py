from datetime import datetime

# Enter the two dates to compare
date1_str = input("Enter the first date in format 'YYYY-MM-DD HH:MM:SS': ")
date2_str = input("Enter the second date in format 'YYYY-MM-DD HH:MM:SS': ")


date1 = datetime.strptime(date1_str, '%Y-%m-%d %H:%M:%S')
date2 = datetime.strptime(date2_str, '%Y-%m-%d %H:%M:%S')


diff = abs((date2 - date1).total_seconds())


print(diff)
