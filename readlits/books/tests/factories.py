import factory


class GenreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "books.Genre"


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "books.Book"
