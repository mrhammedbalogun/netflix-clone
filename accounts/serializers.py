from django.contrib.auth.models import User
from rest_framework import serializers

# from .models import *


class RegisterationSerializer(serializers.ModelSerializer):

	password2 = serializers.CharField(style = {'input_type' : 'password'}, write_only = True)
	
	class Meta:
		model = User
		fields = ['username', 'email', 'password', 'password2']
		extra_kwargs = {
			'password': {'write_only' : True},
			'email': {'required' : True}
		}


	
	def save(self):
		email = self.validated_data['email']
		username = self.validated_data['username']
		password = self.validated_data['password']
		password2 = self.validated_data['password2']
		
		
		user = User (
				email = email,
				username = username,
			)
			
		
		if email == "":
			raise serializers.ValidationError({
				'email': 'Email cannot be empty.'
			})
		
		if User.objects.filter(email=email).exists():
			raise serializers.ValidationError({
				'email': 'Email already exists.'
			})
			
		if password != password2:
			raise serializers.ValidationError({
				'password': 'Passwords must match.'
			})
			
		user.set_password(password)
		user.save()
		
		return user
		
