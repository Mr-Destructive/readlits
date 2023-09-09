from readlits.accounts.tests.factories import AuthorFactory, UserFactory


class TestUser:
    def test_factory(self):
        user = UserFactory()

        assert user is not None


class TestAuthor:
    def test_factory(self):
        author = AuthorFactory(name="test_author")

        assert author is not None
        assert author.__str__() == "test_author"
