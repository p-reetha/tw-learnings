affordable_books_objects = []


class Author:

    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality


class Book:

    def __init__(self, name, price, author):
        self.name = name
        self.__price = price
        self.author = author

    def get_price(self):
        return self.__price

    def affordable_books(self):
        if self.__price <= 1000:
            affordable_books_objects.append(self)


def price_of_all_books(books):
    books_price = 0
    for book in books:
        books_price += book.get_price()
    return books_price


def number_of_books_written_by_author(author_to_search):
    count = 0
    for book in book_objects_list:
        if book.author == author_to_search:
            count += 1
    return count


no_of_books = int(input("Enter the total number of books: "))
author_name_list = []
book_objects_list = []
for book in range(no_of_books):
    print("Enter the details of book{}".format(book+1))
    book_name = input("Enter the book name: ")
    book_price = int(input("Enter the price of the book: "))
    author_name = input("Enter the name of the book author: ")
    if author_name not in author_name_list:
        author_name_list.append(author_name)
        author_age = int(input("Enter the age of the author: "))
        author_nationality = input("Enter the nationality of the author: ")
        author_object = Author(author_name, author_age, author_nationality)
    book_object = Book(book_name, book_price, author_name)
    book_object.affordable_books()
    book_objects_list.append(book_object)
print("\nPrice of all the books: {}\n".format(price_of_all_books(book_objects_list)))
print(author_name_list)
author_books_to_count = input("Enter any of the author names shown above to display the total number of books written by them: ")
print("\nTotal number of books written by {0} is {1}".format(author_books_to_count, number_of_books_written_by_author(author_books_to_count)))
print("\nAffordable Books: ")
for book in affordable_books_objects:
    print("Book name: {0} - Author name: {1}".format(book.name, book.author))
'''
Sample Output:
Enter the total number of books: 6
Enter the details of book1
Enter the book name: python
Enter the price of the book: 999
Enter the name of the book author: guido van rossum
Enter the age of the author: 64
Enter the nationality of the author: dutch
Enter the details of book2
Enter the book name: scala
Enter the price of the book: 1500
Enter the name of the book author: martin odersky
Enter the age of the author: 61
Enter the nationality of the author: german
Enter the details of book3
Enter the book name: java
Enter the price of the book: 800
Enter the name of the book author: james gosling
Enter the age of the author: 65
Enter the nationality of the author: canadian
Enter the details of book4
Enter the book name: C
Enter the price of the book: 1999
Enter the name of the book author: dennis ritchie
Enter the age of the author: 79
Enter the nationality of the author: american
Enter the details of book5
Enter the book name: C++
Enter the price of the book: 1499
Enter the name of the book author: bjame stroustrup
Enter the age of the author: 69
Enter the nationality of the author: danish
Enter the details of book6
Enter the book name: generic java
Enter the price of the book: 599
Enter the name of the book author: martin odersky

Price of all the books: 7396

['guido van rossum', 'martin odersky', 'james gosling', 'dennis ritchie', 'bjame stroustrup']
Enter any of the author names shown above to display the total number of books written by them: martin odersky

Total number of books written by martin odersky is 2

Affordable Books: 
Book name: python - Author name: guido van rossum
Book name: java - Author name: james gosling
Book name: generic java - Author name: martin odersky
'''
