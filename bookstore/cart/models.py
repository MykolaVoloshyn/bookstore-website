from django.db import models
from customers.models import Customer
from books.models import Book


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    # saves timestamp of an order creation
    date_of_order = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    phone = models.CharField(max_length=12, help_text="+1**********")
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)

    @property
    def get_price_of_order(self):
        ordered_items = self.ordereditem_set.all()
        total_price = sum([item.get_total_price for item in ordered_items])

        return total_price

    @property
    def get_number_of_items(self):
        ordered_items = self.ordereditem_set.all()
        total_quantity = sum([item.quantity for item in ordered_items])

        return total_quantity

    def __str__(self) -> str:
        return f"Order №{self.id}"


class OrderedItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveSmallIntegerField(default=1)
    # saves timestamp when a book was added to an order
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total_price(self):
        total_price = self.book.get_price * self.quantity

        return total_price
