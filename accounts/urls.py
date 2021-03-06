from django.contrib import admin
from django.urls import path, include
from . import views 
from . views import *


app_name = "accounts"

urlpatterns = [
	path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/register/', Registeration.as_view(), name = "register"),
    #path('', views.HomePage, name='home')
  


]