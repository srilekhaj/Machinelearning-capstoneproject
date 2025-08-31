# Create your models here.
from django.db import models

# Create your models here.
class cpredModel(models.Model):

    age=models.FloatField()
    bmi=models.FloatField()
    children=models.FloatField()
    sex_male = models.IntegerField()
    smoker_yes=models.FloatField()
    region_southeast=models.FloatField()
