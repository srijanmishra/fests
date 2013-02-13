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


class EventRegistration(models.model):
	team_name = models.CharField(max_length=30)
	team_representative = models.CharField(max_length=30)
	representative_contact = models.BigIntegerField()
	branch = models.CharField(max_length=30)
	event = models.CharField(max_length=100)
	member_2_details = models.CharField(max_length=500)
	member_3_details = models.CharField(max_length=500)
	member_4_details = models.CharField(max_length=500)
	member_5_details = models.CharField(max_length=500)

	def __unicode__(self):
		return '%s - %s' % (self.event,self.team_name)

	def __str__(self):
		return '%s - %s' % (self.event,self.team_name)
