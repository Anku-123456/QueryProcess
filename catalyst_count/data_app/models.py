from django.db import models

class CompanyData(models.Model):
    name = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    revenue = models.FloatField()

    def __str__(self):
        return self.name
