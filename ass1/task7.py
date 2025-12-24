# days = years, weeks and days
# 375 = 1 year, 1 week and 3 days
# 375 // 365 = 1 year
# 375 % 365 = 10 // 7 = 1 week
# 375 % 365 = 10 % 7 = 3 days
d = int(input("Enter number of days :"))
years = d//365
weeks = (d % 365) // 7
days = (d % 365) % 7
print("Years =",years,"\nWeeks =",weeks,"\nDays =",days)











