# William Vann
# module5_part1.py

# ask user for number of years for data collection

num_years = int(input('Enter the number of years: \n'))
if num_years <= 0:
    print('Number of years must be > 0, defaulting to 1')
    num_years = 1 

# initialize variables
num_months = 0
total_rainfall = 0

# outer loop for years
for year in range(1,num_years+1):
    
    # inner loop for months
    for month in range(1,13):
        
        # ask user for number of inches of rain for month in question
        rain_inches = int(input(f'Enter inches of rainfall for year {year} month {month}: \n'))
        # increment rainfall totals and number of months
        total_rainfall += rain_inches
        num_months += 1

# calculate average rainfall per month
avg_rainfall_per_month = round((total_rainfall / num_months), 2)

# output results to user 
print(f'Total months: \t\t\t\t{num_months}') 
print(f'Total rainfall (in.): \t\t\t{total_rainfall}')
print(f'Average rainfall per month (in.): \t{avg_rainfall_per_month}')