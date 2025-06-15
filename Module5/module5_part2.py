# William Vann
# module5_part2.py

# initialize books to points dictionary
books_to_points = {
    0:0,
    1:0,
    2:5,
    3:5,
    4:15,
    5:15,
    6:30,
    7:30,
    8:60
}

# ask user for number of books bought
num_books_bought = int(input('Enter the number of books bought this month: \n'))

# conditional logic to tell user how many points they've earned
if num_books_bought in books_to_points:
    print(f"You've earned {books_to_points[num_books_bought]} points!")
elif num_books_bought > 8:
    print(f"You've earned {books_to_points[8]} points!")
else:
    print("Sorry, you haven't earned any points yet!")