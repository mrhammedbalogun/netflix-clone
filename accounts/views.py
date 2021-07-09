from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from .serializers import *


# Create your views here.
class Registeration(APIView):
	
	serializer_class = RegisterationSerializer
	
	permission_classes = [permissions.AllowAny]
	
	def post(self, request):
		"""
		Registers a new user
		"""
		data = {}
		if request.method == "POST":
			serializer = self.serializer_class(data = request.data)
			
			if serializer.is_valid():
				username = request.POST['username']
				serializer.save()
				# data[ 'response' : f'successfully registered user {username}',]
				return Response(serializer.data, status = status.HTTP_201_CREATED)

			return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class ListUsers(APIView):
	"""
	View to list all users in the system.

	* Requires token authentication.
	* Only admin users are able to access this view - (can be modified to any authenticated user.)
	"""
	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.IsAdminUser]
	# permission_classes = [permissions.IsAuthenticated]

	def get(self, request, format=None):
		"""
		Return a list of all users.
		"""
		usernames = [user.username for user in User.objects.all()]
		return Response(usernames)
		



class CustomAuthToken(ObtainAuthToken):
	
	def post(self, request, *args, **kwargs):
		"""
		Grabbing the tokens associated with a user
		"""
		serializer = self.serializer_class(data=request.data,
					context={'request': request})
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user']
		token, created = Token.objects.get_or_create(user=user)
		
		return Response({
			'token': token.key,
			'user_id': user.pk,
			'email': user.email
		})
