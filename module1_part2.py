# get input
num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))    

# print results
print(f'{num1} times {num2} = {num1 * num2}')

# check for division by zero
if num2 != 0:   
    print(f'{num1} divided by {num2} = {num1 / num2}')  
else:
    print(f'{num1} divided by {num2} = Cannot divide by zero!')