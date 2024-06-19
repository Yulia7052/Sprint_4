from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_init_books_genre(self, collector):
        assert collector.get_books_genre() == {}

    def test_init_favorites(self, collector):
        assert collector.get_list_of_favorites_books() == []

    def test_add_new_book_book_len(self, collector):
        collector.add_new_book('Жареные зелёные помидоры в кафе "Полустанок"')
        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_positive_inputs(self, genre, collector):
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.set_book_genre('Гарри Поттер и философский камень', genre)
        assert collector.get_book_genre('Гарри Поттер и философский камень') == genre

    def test_get_book_genre_negative_input(self, collector):
        assert collector.get_book_genre('Унесенные ветром') == None

    @pytest.mark.parametrize(
        'genre_1,genre_2',
        [
             ['Фантастика', 'Ужасы'],
             ['Ужасы', 'Детективы'],
             ['Детективы', 'Мультфильмы'],
             ['Мультфильмы', 'Комедии'],
             ['Комедии', 'Фантастика']
        ]
    )
    def test_get_books_with_specific_genre_positive_inputs(self, genre_1, genre_2):
        collector = BooksCollector()
        collector.add_new_book('Мгла')
        collector.add_new_book('Гнев ангелов')
        collector.set_book_genre('Мгла', genre_1)
        collector.set_book_genre('Гнев ангелов', genre_2)
        books = collector.get_books_with_specific_genre(genre_1)
        assert len(books) == 1 and books[0] == 'Мгла'

    def test_get_books_genre_positive(self, collector):
        collector.add_new_book('Преступление и наказание')
        assert collector.get_books_genre() == collector.books_genre

    def test_get_books_for_children_only_children_books(self):
        collector = BooksCollector()
        collector.add_new_book('Доктор Айболит')
        collector.add_new_book('Под куполом')
        collector.add_new_book('Кто-то следит за мной')
        collector.set_book_genre('Доктор Айболит', 'Мультфильмы')
        collector.set_book_genre('Под куполом', 'Ужасы')
        collector.set_book_genre('Кто-то следит за мной', 'Детективы')
        books_for_children = collector.get_books_for_children()
        assert len(books_for_children) == 1 and books_for_children[0] == 'Доктор Айболит'

    def test_add_book_in_favorites_add_book(self, collector):
        collector.add_new_book('Королева Марго')
        collector.add_book_in_favorites('Королева Марго')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_clear(self, collector):
        collector.add_new_book('Дон Жуан')
        collector.add_book_in_favorites('Дон Жуан')
        collector.delete_book_from_favorites('Дон Жуан')
        assert len(collector.get_list_of_favorites_books()) == 0


    def test_get_list_of_favorites_books_positive(self, collector):
        collector.add_new_book('Анжелика и Султан')
        collector.add_book_in_favorites('Анжелика и Султан')
        assert collector.get_list_of_favorites_books() == collector.favorites