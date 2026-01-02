''' Time modification example'''

def solution(time, seconds):
    time_parts = [int(part) for part in time.split(":")]
    seconds_since_start = time_parts[0] * 3600 + time_parts[1] * 60 + time_parts[2]
    total_seconds = (seconds_since_start + seconds) % (24 * 3600)
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

''' More time string modification work - these are problems to solve '''

''' Example 1 
You are given two input arguments: an array of strings timePoints and an integer added_seconds. Each string in timePoints is in the HH:MM:SS format, representing a valid time from "00:00:00" to "23:59:59" inclusive. 
The integer added_seconds represents a number of seconds, ranging from 1 to 86,400. Your task is to create a new function, add_seconds_to_times(timePoints, added_seconds), 
which takes these two arguments and returns a new array of strings. 
Each string in the returned array is the new time, calculated by adding the provided added_seconds to the corresponding time in timePoints, formatted in HH:MM:SS.

The array timePoints contains n strings, where n can be any integer from 1 to 100 inclusive. The time represented by each string in timePoints is guaranteed to be valid. 
The total time, after adding added_seconds, can roll over to the next day.

Example

For timePoints = ['10:00:00', '23:30:00'] and added_seconds = 3600, the output should be ['11:00:00', '00:30:00'].'''

def add_seconds_to_times(timePoints, added_seconds):
    return [solution(time, added_seconds) for time in timePoints]

print(add_seconds_to_times(['10:00:00', '23:30:00'], 3600))  # ['11:00:00', '00:30:00']

''' Example 2
You are given a time period formatted as a string in the HH:MM:SS - HH:MM:SS format. HH:MM:SS represents the time in hours, minutes, and seconds form, and the hyphen (-) separates the start time from the end time of the period.

Your task is to calculate how many minutes pass from the start time until the end time.

Here are some guidelines:

    The input times are always valid time strings in the HH:MM:SS format, with HH ranging from 00 to 23, and MM and SS from 00 to 59.
    The output should be an integer, representing the total length of the time period in minutes.
    The start time of the period will always be earlier than the end time, so periods that cross over midnight (like 23:00:00 - 01:00:00) are not considered.
    We are interested in the number of times the time passes some HH:MM:00 after the start time until the end time. Any remaining seconds should be disregarded; 
    for instance, a period of "12:15:00 - 12:16:59" represents 1 minute, not 2, and a period of "12:14:59 - 12:15:00" also represents 1 minute.

'''

def time_period_length(time_period):
    # Your code goes here
    start_time, end_time = time_period.split(" - ")
    start_parts = list(map(int, start_time.split(":")))
    end_parts = list(map(int, end_time.split(":")))

    # convert start and end times to total minutes
    start_minutes = start_parts[0] * 60 + start_parts[1]
    end_minutes = end_parts[0] * 60 + end_parts[1] 

    diff_minutes = end_minutes - start_minutes

    return diff_minutes


print(time_period_length("12:15:30 - 14:00:00"))  # should return 105


''' Example 3
You are given an initial date as a string in the format YYYY-MM-DD, along with an integer n which represents a number of days. 
Your task is to calculate the date after adding the given number of days to the initial date and return the result in the YYYY-MM-DD format.

Keep these points in mind when resolving the task:

    The initial date string is always valid, formatted as YYYY-MM-DD, where YYYY denotes the year, MM the month, and DD the day.
    The given integer n is the number of days you have to add to the initial date and will be up to 50,00050,000.
    The output should be a string showcasing the final date after adding n days, in the YYYY-MM-DD format.

Your function will be in the form add_days(date: str, n: int) -> str.

Constraints

    date = the date string in the YYYY-MM-DD format. The year YYYY will be from 1900 to 2100, inclusive. The month MM and the day DD will be valid for the given year.
    n = the integer representing the number of days you have to add to the initial date. n ranges from 1 to 50,00050,000, inclusive.
    You should consider leap years in the calculation. A year is a leap year if it is divisible by 4, but century years (years divisible by 100) are not leap years unless they are divisible by 400. 
    This means that the year 2000 was a leap year, although 1900 was not.
    The month and day result should always be two digits long, padding with a 0 if necessary. For example, July 9th should be formatted as "07-09".

Example

For date = '1999-01-01' and n = 365, the output should be '2000-01-01'.'''

def add_days(date, n):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year, month, day = map(int, date.split('-'))

    # Check for leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[2] = 29 
    else:
        days_in_month[2] = 28

    print(f"Initial date: {year}-{month:02d}-{day:02d}, adding {n} days")
    print(f"The year is {year}")
    if days_in_month[2] == 29:
        print(f"{year} is a leap year, February has {days_in_month[2]} days.")
    else:
        print(f"{year} is not a leap year, February has {days_in_month[2]} days.")

    # Add n days
    day += n
    while day > days_in_month[month]:
        day -= days_in_month[month]
        month += 1
        
        if month > 12:
            month = 1
            year += 1
            # Check for leap year again
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                days_in_month[2] = 29 
            else:
                days_in_month[2] = 28


    # Format the result
    date_after_n_days = f"{year:04d}-{month:02d}-{day:02d}"

    return date_after_n_days

print(add_days('2000-02-01', 28))  # should return '2000-01-01'