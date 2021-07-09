from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models import Model
from django.contrib.auth.models import User

# Create your models here.



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	'''
	Create token for user on login
	'''
	if created:
		Token.objects.create(user=instance)


class next_of_kin(models.Model):
	user = models.OneToOneField(User, on_delete= models.CASCADE)
	email =models.EmailField(max_length=30)
	
	def  __str__(self):
		return self.email