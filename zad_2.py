# Zadanie 2 lab_4
from klasy.klasa_library import Library
from klasy.klasa_order import Order
from klasy.klasa_employee import Employee
from klasy.klasa_book import Book
from klasy.klasa_student import Student

if __name__ == '__main__':
    library_1 = Library("Katowice", "Bogucicka 4","40-000", "9:00-18:00", "700700700")
    library_2 = Library("Sosnowiec", "Prosta 7", "41-200", "8:300-19:00", "800800800")

    book_1 = Book(library_1, "2013-05-23", "Adam", "Słowacki", 1200)
    book_2 = Book(library_1, "2017-12-06", "Juliusz", "Mickiewicz", 1354)
    book_3 = Book(library_1, "2020-08-23", "Wojciech", "Dunia", 111)
    book_4 = Book(library_2, "2004-11-11", "Małgorzata", "Domagalik", 120)
    book_5 = Book(library_2, "2022-12-31", "Jan", "Nowak", 542)

    emp_1 = Employee("Adam", "Małysz", "2020-01-01", "1975-02-02", "Katowice", "Prosta 23", "40-000", "123456789")
    emp_2 = Employee("Mariusz", "Pudzianowski", "2019-01-01", "1970-02-02", "Kraków", "Krzywa 32", "50-00", "987654321")
    emp_3 = Employee("Thiago", "Cionek", "2018-01-01", "1977-02-02", "Warszawa", "Długa 123", "60-000", "567894321")

    student_1 = Student("Adam", 67)
    student_2 = Student("Kasia", 32)
    student_3 = Student("Jan", 99)

    order_1 = Order(emp_1, student_2, book_5, "2021-11-06")
    order_2 = Order(emp_3, student_3, book_3, "2020-12-27")

    print(order_1)
    print(order_2)

