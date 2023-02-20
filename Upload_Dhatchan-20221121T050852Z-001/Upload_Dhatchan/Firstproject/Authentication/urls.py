from django.urls import path
from . import views 
urlpatterns=[
	path('login',views.Auth.login),
	path('login_data',views.Auth.login_data)
	
]
