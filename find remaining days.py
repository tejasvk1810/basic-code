#find remaining days

days=int(input("Enter the no. of days :"))
year=days/365
temp=days%365
month=days/30
week=(days/7)
print("total days :",days)
print("total year :",year)
print("total temp :",temp)
print("total month :",month)
print("total week :",week)