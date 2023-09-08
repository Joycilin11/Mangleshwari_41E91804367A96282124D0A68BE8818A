def isLeapYear(year):
  if(year % 4 and year % 100!=0 or year % 400==0):
    return True
  else:
    return false 
year=int(input("Enter a year:"))
if isLeapYear(year):
  print("{} is a Leap year.". format (year))
else:
  print ("{} is not a Leap year.". format (year))