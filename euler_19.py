from datetime import datetime

def is_sunday(date):
    date = datetime.strptime(date, '%Y-%m-%d')
    day_index = date.weekday()
    if day_index == 6:
        return True

def calculate_days():
    sum = 0
    for year in range(1901,2001):
        for month in range(1,13):
            if is_sunday(f"{year}-{month}-1"):
                sum += 1
    print(sum)


calculate_days()