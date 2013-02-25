from django.db import models

class Sender(models.Model):
	number = models.IntegerField(primary_key=True)

	def __unicode__(self):
        	return u"%s" % (self.number)
	
class Data(models.Model):
	temperature = models.FloatField()
	humidity = models.FloatField()
	windvelocity = models.FloatField()
	sender = models.ForeignKey(Sender)

	def __unicode__(self):
        	return u"%s %s %s" % (self.temprature, self.humidity, self.windvelocity)
