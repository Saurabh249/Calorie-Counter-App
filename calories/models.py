from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from datetime import date

# Create your models here.


class Food(models.Model):
	name = models.CharField(max_length=200 ,null=False)
	quantity = models.PositiveIntegerField(null=False,default=0)
	calorie = models.FloatField(null=False,default=0)
	person_of = models.ForeignKey(User,null=True,on_delete=models.CASCADE)

	def __str__(self):
		return self.name


class Profile(models.Model):
	person_of = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
	calorie_count = models.FloatField(null=True,blank=True,default=0)
	food_selected = models.ForeignKey(Food,on_delete=models.CASCADE,null=True,blank=True)
	quantity = models.PositiveIntegerField(default=0)
	total_calorie = models.FloatField(default=0,null=True)
	date = models.DateField(auto_now_add=True)

	
	def save(self, *args, **kwargs):# new
		if self.food_selected != None:
			self.amount = (self.food_selected.calorie/self.food_selected.quantity) 
			self.calorie_count = self.amount*self.quantity
			self.total_calorie = self.calorie_count + self.total_calorie     
			super(Profile, self).save(*args,**kwargs)
		else:
			super(Profile, self).save(*args,**kwargs)


	def __str__(self):
		return str(self.person_of.username)

def create_profile(sender,instance,created,**kwargs):
	if created:
		Profile.objects.create(person_of=instance)
		print("profile created")

post_save.connect(create_profile,sender=User)


def update_profile(sender,instance,created,**kwargs):
	if created == False:
		Person = instance
		present_time = date.today()
		print("Hi there")
		if present_time>Person.date:
			Profile.objects.create(person_of=instance.person_of,total_calorie=0)

post_save.connect(update_profile,sender=Profile)
