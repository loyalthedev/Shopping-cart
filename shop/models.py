from django.db import models

# Create your models here.
from django.db import models


# class Brand(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


class Headphones(models.Model):
    brand = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # image = models.ImageField(
    #     upload_to='headphones_images/', blank=True, null=True)

    def __str__(self):
        return self.name

# class Review(models.Model):
#     headphones = models.ForeignKey(Headphones, on_delete=models.CASCADE, related_name='reviews')
#     author_name = models.CharField(max_length=100)
#     content = models.TextField()
#     rating = models.PositiveIntegerField()

    # def __str__(self):
    #     return f'{self.headphones} - {self.author_name}'
