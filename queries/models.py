from django.db import models

# Create your models here.


LANGUAGE_TYPE_CHOICES = (
        ('O', 'Object Oreanted programming'),
        ('F', 'Functional programming'),
    )


class Location(models.Model):
    country = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    municipality = models.CharField(max_length=64)
    streat = models.CharField(max_length=64)
    building_number = models.IntegerField()
    branch_id = models.CharField(max_length=90)

    def __str__(self):
        return f'{self.city} - {self.country}'


class Company(models.Model):
    name = models.CharField(max_length=64)
    created_date = models.DateTimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=64)
    created_date = models.DateTimeField()
    type = models.CharField(max_length=300, choices = LANGUAGE_TYPE_CHOICES)
    descripton = models.TextField()

    def __str__(self):
        return self.name


class Programmer(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    joined_date = models.DateTimeField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name
