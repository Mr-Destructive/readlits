from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(
        "accounts.Author",
        on_delete=models.CASCADE,
    )
    genre = models.ManyToManyField("books.Genre", related_name="books", blank=True)
    published = models.DateField(auto_now_add=True)
    cover_image = models.ImageField(upload_to="covers/", blank=True, null=True)

    def __str__(self):
        return self.title
