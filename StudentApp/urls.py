from django.urls import path

from StudentApp import views

urlpatterns = [
    path('', views.log_fun, name='log'),  # it will display login.html page
    path('logindata', views.logdata_fun),  # it will read data and user is superuser redirect to home.html page
    path('Reg', views.reg_fun, name='Reg'),  # it will redirect to register.html page
    path('read', views.regdata_fun),  # it will create superuser account
    path('home', views.home_fun, name='home'),  # it will redirect to home.html
    path('add_students', views.addstudent_fun, name='add'),
    path('readdata', views.readdata_fun),
    path('studentdisplay', views.studentdsply_fun, name='studentdisplay'),
    path('update/<int:id>', views.update_fun, name='update'),
    path('delete/<int:id>', views.delete_fun, name='delete'),
    path('log_out', views.logout_fun, name='log_out')

]
