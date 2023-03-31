calendar={
    'january':31,
    'february':28 or 29,
    'march':31,
    'april':30,
    'may':31,
    'june':30,
    'july':31,
    'august':31,
    'september':30,
    'october':31,
    'november':30,
    'december':31   
          }

month=input('Enter a month:')
print()
print('The number of days in that month is',calendar[month.lower()])
print()
months=list(calendar.keys())
months.sort()
print('The months in alphabetical order:')
print()
for i in months:
    print(i)
print('The months with 31 days are:')
items=list(calendar.items())
for i in items:
    if i[1]==31:
        print(i[0])
print('\nThe pairs sorted by the number of days in each month.')

sorted_days_in_month = sorted(items, key=lambda x: x[1])


for month, days in sorted_days_in_month:
    print(month, ":", days)
