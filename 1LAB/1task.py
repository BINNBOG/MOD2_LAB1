class Pet:
    '''class домашнего питомца, имеет 4 аргумента
    name - имя питомец
    race - вид питомца (кот, собака, птица ...)
    paws - кол-во лап
    sound - какой звук издает

    Example info():
    >>> info()
    The cat's name is Barsik.
    Barsik has 3 paws.
    It makes sound like myu.

    Example sound():
    >>> sound()
    myu
    '''
    def __init__(self, name: str, race: str, paws: int, sound: str) -> None:
        self.name = name
        if not isinstance(paws, int):
            raise TypeError
        elif paws < 0:
            raise ValueError
        self.paws = paws
        self.p_sound = sound
        self.race = race


    def sound(self) -> None:
        #метод выводит звук, который издает питомец
        print(self.p_sound)


    def info(self) -> None:
        #метод выводит информацию о питомце
        print(f"The {self.race}'s name is {self.name}.\n"
              f"{self.name} has {self.paws} paws.\n"
              f"It makes sound like {self.p_sound}.\n")


class Book:
    '''
    class книга, имеет 4 аргумента
    name - название книги
    pages - кол-во страниц
    author - автор
    now_page - текущая страница для чтения

    Example info():
    >>> info()
    Book's name: Crime and punishment.
    Count of pages: 10.
    Author Fedor Dostoevskie.

    Example next_page():
    >>> next_page()
    Книга закончилась!   ---- если текущая страница превышает или равна страницам книги
    '''
    def __init__(self, name: str, pages: int, author: str) -> None:
        self.name = name
        self.author = author
        if not isinstance(pages, int):
            raise TypeError
        elif pages < 0:
            raise ValueError
        self.pages = pages
        self.now_page = 0


    def next_page(self) -> None:
        #метод для переворота страницы
        if self.now_page < self.pages:#преверка на превышение страниц
            self.now_page += 1
        else:
            print("Книга закончилась!")


    def info(self) -> None:
        #метод выводит информацию о книге
        print(f"Book's name: {self.name}.\n"
              f"Count of pages: {self.pages}.\n"
              f"Author {self.author}.\n")


class Person:
    '''class человека, имеет 4 аргумента
    name - имя человека
    surname - фамилия человека
    age - возраст
    sex - пол человека (male, female)

    Example info:
    >>> info()
    Ivan Ivanov, 16 years old, sex: male.

    '''
    def __init__(self, name: str, surname: str, age: int, sex: str) -> None:
        self.name = name
        self.surname = surname
        if not isinstance(age, int):
            raise TypeError
        elif age < 0:
            raise ValueError
        self.age = age
        if sex == "male" or sex == "female":
            self.sex = sex
        else:
            raise ValueError


    def info(self) -> None:
        #функция выводит информацию о человеке
        print(f"{self.name} {self.surname}, {self.age} years old, "
              f"sex: {self.sex}.")


    def happy_birthday(self) -> None:
        #прибавляет к возрасту один
        self.age += 1


if __name__ == "__main__":
    person1 = Person("Ivan", "Ivanov", 16, "male")
    p_book = Book("Crime and punishment", 10, "Fedor Dostoevskie")
    pet1 = Pet("Barsik", "cat", 3, "myu")
    pet1.info()
    p_book.info()
    person1.info()
