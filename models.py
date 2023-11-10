from django.db import models

AVAILABILITY_CHOICES = (
    ('a', 'Available'),
    ('o', 'On Loan'),
    ('r', 'Reserved'),
    ('m', 'Maintenance'),
)

class Record(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    description = models.TextField()
    format = models.CharField(max_length=50)
    availability_status = models.CharField(max_length=1, choices=AVAILABILITY_CHOICES)
    due_back = models.DateField(null=True, blank=True)

class CD(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    description = models.TextField()
    format = models.CharField(max_length=50)
    availability_status = models.CharField(max_length=1, choices=AVAILABILITY_CHOICES)
    due_back = models.DateField(null=True, blank=True)

class Cassette(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    description = models.TextField()
    format = models.CharField(max_length=50)
    availability_status = models.CharField(max_length=1, choices=AVAILABILITY_CHOICES)
    due_back = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

class Equipment(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  description = models.TextField()
  availability_status = models.CharField(max_length=1, choices=AVAILABILITY_CHOICES)
  due_back = models.DateField(null=True, blank=True)
