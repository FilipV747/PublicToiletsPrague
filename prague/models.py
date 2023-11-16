from django.db import models
from django.shortcuts import reverse
import uuid
class Toilet(models.Model):
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    price = models.CharField(max_length=100, null=True, blank=True)
    schedule = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        if self.address:
            return self.address
        else:
            return "No Address"

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = str(uuid.uuid4())[:5]

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('prague:toilet_detail', kwargs={'slug':self.slug})

    def average_rating(self):
            reviews = self.review_set.all()
            if not reviews:
                return 0
            total_rating = 0
            for review in reviews:
                total_rating += review.rating
            avg = total_rating / len(reviews)
            return avg


RATINGS_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)
class Review(models.Model):
    username = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    toilet = models.ForeignKey(Toilet, on_delete=models.PROTECT)
    rating = models.PositiveIntegerField(choices=RATINGS_CHOICES, default=1)
    date_posted = models.DateTimeField(auto_now_add=True)

