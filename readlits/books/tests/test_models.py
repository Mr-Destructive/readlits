from readlits.accounts.tests.factories import AuthorFactory
from readlits.books.tests.factories import BookFactory, GenreFactory


class TestGenre:
    def test_factory(self):
        genre = GenreFactory(name="test_genre")
        assert genre is not None
        assert genre.__str__() == "test_genre"


class TestBook:
    def test_factory(self):
        author = AuthorFactory()
        book = BookFactory(title="test_book", author=author)

        assert book is not None
        assert book.__str__() == "test_book"
