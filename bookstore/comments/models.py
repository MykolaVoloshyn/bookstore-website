from django.db import models
from books.models import Book
from customers.models import Customer


class Comment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    text = models.TextField(max_length=5000)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer} - {self.book}"
