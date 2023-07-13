import calendar
#


full_date = input("Enter a date: ")
day = int(full_date[:2])
month = int(full_date[3:5])
year = int(full_date[6:])
weekdays = ['Monday', "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]
weekday_index = calendar.weekday(year, month, day)
print(weekdays[weekday_index])


# Course solution:

# import calendar
# date = input("Enter a date: ")
# day = int(date[:2])
# month = int(date[3:5])
# year = int(date[6:])
# weekday=calendar.weekday(year,month,day)
# if weekday == 0:
#     print("Monday")
# if weekday == 1:
#     print("Tuesday")
# if weekday == 2:
#     print("Wednesday")
# if weekday == 3:
#     print("Thursday")
# if weekday == 4:
#     print("Friday")
# if weekday == 5:
#     print("Saturday")
# if weekday == 6:
#     print("Sunday")