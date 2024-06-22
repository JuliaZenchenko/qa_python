import pytest

from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book("Аватар")
        assert collector.books_genre.get("Аватар") == ''

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Аватар")
        collector.set_book_genre("Аватар", "Фантастика")
        assert collector.books_genre.get("Аватар") == "Фантастика"

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Аватар")
        collector.set_book_genre("Аватар", "Фантастика")
        assert collector.get_book_genre("Аватар") == "Фантастика"

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Аватар")
        collector.set_book_genre("Аватар", "Фантастика")
        assert "Аватар" in collector.get_books_with_specific_genre("Фантастика")

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Аватар")
        collector.set_book_genre("Аватар", "Фантастика")
        assert collector.get_books_genre() == {"Аватар": "Фантастика"}

    @pytest.mark.parametrize("name, genre", [("Аватар", "Фантастика"), ("Маугли", "Мультфильмы")])
    def test_get_books_for_children(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert name in collector.get_books_for_children()

    @pytest.mark.parametrize("name", ["Аватар", "Маугли", "Сказки"])
    def test_delete_book_from_favorites(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name[0])
        assert name[0] not in collector.favorites

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book("Аватар")
        collector.add_book_in_favorites("Аватар")
        assert collector.get_list_of_favorites_books() == ["Аватар"]

    def test_add_some_books_and_check_count(self):
        collector = BooksCollector()
        books_to_add = ["Аватар", "Маугли", "Сказки"]
        for book in books_to_add:
            collector.add_new_book(book)
        assert len(collector.books_genre) == len(books_to_add)
