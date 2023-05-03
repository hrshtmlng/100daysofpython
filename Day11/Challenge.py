daysThisYear = int(input("How many days are in this year?"))

daysInYear = 365
daysInLeapyear = 366
hoursInDay = 24
minutesInHour = 60
secondsInMinute = 60

result = daysInYear * hoursInDay * minutesInHour * secondsInMinute

leapyearResult = daysInLeapyear * hoursInDay * minutesInHour * secondsInMinute

if daysThisYear == 366:
  print("Number of seconds in a leap year are", leapyearResult)
else:
  print("Number of seconds in a year are", result)

