from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.contrib.auth.decorators import login_required
from . import views
urlpatterns=[
	path("login",views.login_form.login),
	path("add_Staff",login_required(views.Staff_All.Add_Staff)),
	path("display_Staff",login_required(views.Staff_All.Display_Staff)),
	path("forgot_password",views.login_form.forgot_password),
	path("Ver_Otp",views.login_form.Ver_Otp),
	path("change_password",views.login_form.change_password),
	path("update_Staff",login_required(views.Staff_All.Update_Staff)),
	path("remove_Staff",login_required(views.Staff_All.Remove_Staff)),
	path("back_to_admin",login_required(views.Staff_All.Back_to_Admin)),
	path("student",login_required(views.Student_All.Student)),
	path("display_student",login_required(views.Student_All.Display_Student)),
	path("add_Student",login_required(views.Student_All.Add_Student)),
	path("update_Student",login_required(views.Student_All.Update_Student)),
	path("remove_Student",login_required(views.Student_All.Remove_Student)),
	path("Admin_Edit_Attendance",login_required(views.Student_All.Admin_Edit_Attendance)),
	path("Admin_Edited_Mark_Attendance",login_required(views.Student_All.Admin_Edited_Mark_Attendance)),
]

#path('', image_request, name = "image-request"),
