num_years = int(input('Enter the number of years: \n'))
num_months = 0
total_rainfall = 0

for year in range(num_years):
    for month in range(1,13):
        rain_inches = int(input(f'Enter number of inches of rainfall for year {year} month {month}: \n'))
        total_rainfall += rain_inches
        num_months += 1

avg_rainfall_per_month = total_rainfall / num_months

print(f'Total months: {num_months}') 
print(f'Total rainfall (in.): {total_rainfall}')
print(f'Average rainfall (in.) per month: {avg_rainfall_per_month}')