from django.db import models

class Reg_User(models.Model):
    GENDER_CHOICES = (
                      ('M', 'male'),
                      ('F', 'female'),
                      )
    name = models.CharField(max_length=30)
    email = models.EmailField()
    contact = models.CharField(max_length=30)
    birthday = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    fb_ID = models.BigIntegerField()

    def __unicode__(self):
        return self.name
