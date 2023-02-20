from django.urls import path
from . import views 
urlpatterns=[
	path('murali',views.name.murali),
	path('mk',views.name.mk),
	path('prem',views.name.prem),
	path('html',views.name.Muralihtml),
	path('table',views.Table.display),
	path('New_record',views.Table.Data_Enter),
	path('Div_table',views.css.div_class),
	path('delete/<str:id>',views.Table.delete_data),
	path('update/<str:id>',views.Table.edit_data),
	path('login',views.auth.login),
	
]
