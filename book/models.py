import uuid

from django.db import models


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=150, blank=False, null=False)
    isbn = models.CharField(max_length=13, blank=False, null=False)

    authors = models.ManyToManyField(Author, related_name="books")

    def __str__(self):
        return f"{self.title} - {self.isbn}"
