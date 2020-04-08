from django.db import models

# Creating model here.
class HeartAttackModel(models.Model):
    """
        Reading all data from the form
    """
    age = models.IntegerField()
    sex = models.IntegerField()
    cp = models.IntegerField()
    trestbps  = models.IntegerField()
    chol = models.IntegerField()
    fbs = models.IntegerField()
    restecg = models.IntegerField()
    thalach  = models.IntegerField()
    exang = models.IntegerField()
    oldpeak = models.IntegerField()
    slope = models.IntegerField()
    ca = models.IntegerField()
    thal = models.IntegerField()
