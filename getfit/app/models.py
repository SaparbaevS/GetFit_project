from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class TrainCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TrainStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Train(models.Model):
    name = models.CharField(max_length=150)
    descriptions = models.TextField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    image = models.ImageField(upload_to='training_files')
    category = models.ForeignKey(TrainCategory, on_delete=models.CASCADE)
    status = models.ForeignKey(TrainStatus, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.category} - {self.status}'

    def get_absolute_url(self):
         return reverse("products:detail", args=(self.slug, ))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)