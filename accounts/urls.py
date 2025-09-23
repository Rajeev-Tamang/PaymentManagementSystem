from django.urls import path
from . import views
app_name='accounts'
urlpatterns = [
    path('register/',views.school_admin_register,name='school_admin_register'),
    path('login/',views.login,name='login'),
]