from django.db import models

# Create your models here.
class HeartAttackModel(models.Model):
    age = models.IntegerField(max_length=20)
    sex = models.IntegerField(max_length=100)
    cp = models.IntegerField(max_length=100)
    trestbps  = models.IntegerField(max_length=100)
    chol = models.IntegerField(max_length=6)
    fbs = models.IntegerField('date of birth')
    restecg = models.IntegerField(max_length=15)
    thalach  = models.IntegerField(max_length=100)
    exang = models.IntegerField(max_length=200)
    oldpeak = models.IntegerField(max_length=200)
    slope = models.IntegerField(max_length=200)
    ca = models.IntegerField(max_length=200)
    thal = models.IntegerField(max_length=200)

    # def __str__(self):
    #     return self.age