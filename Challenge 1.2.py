def isleapYear(year):
  if (year%4==0 and year%100!=0) or year%400==0:
    print(year,"is Leap Year")
  else:
    print(year,"is not Leap Year")

year=int(input("Enter a Year:"))
isleapYear(year)