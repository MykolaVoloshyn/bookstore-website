from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=100, blank=False)
    surname = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        ordering = ["name", "surname"]


class Genre(models.Model):
    # first argument changes label name to Genre in admins panel
    name = models.CharField("Genre", max_length=100, blank=False)
    slug = models.SlugField(max_length=100, unique=True, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Publisher(models.Model):
    name = models.CharField(max_length=100, blank=False)
    city = models.CharField(max_length=100, blank=False)
    country = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Book(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL")
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
    year = models.PositiveIntegerField(default=0)
    pages = models.PositiveIntegerField(default=1)
    price = models.FloatField(default=0.00)
    cover = models.FileField(upload_to="books/")
    annotation = models.TextField()
    in_stock = models.BooleanField(default=False)
    new = models.BooleanField(default=True)
    on_sale = models.BooleanField(default=False)
    sale = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("about_book", kwargs={"slug": self.slug})

    @property
    def get_price(self):
        if self.on_sale:
            price = self.price - (self.price / 100 * self.sale)
        else:
            price = self.price
        return price

    class Meta:
        ordering = ["title", "author"]
