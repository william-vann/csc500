points_dict = {
    0: 0,
    2: 5,
    4: 15,
    6: 30,
    8: 60
}
num_books_bought = int(input('Enter the number of books bought this month: \n'))

if num_books_bought in points_dict:
    print(f"You've earned {points_dict[num_books_bought]} points!")
