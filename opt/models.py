from django.db import models

class NewArrivals(models.Model):
    name = models.CharField(max_length=300)
    price = models.CharField(max_length=100)
    image = models.ImageField(upload_to='new arrivals')
    date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name

class Iphones(models.Model):
    name = models.CharField(max_length=300)
    price = models.CharField(max_length=100)
    image = models.ImageField(upload_to='new arrivals')
    date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name

class Samsung(models.Model):
    name = models.CharField(max_length=300)
    price = models.CharField(max_length=100)
    image = models.ImageField(upload_to='new arrivals')
    date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name