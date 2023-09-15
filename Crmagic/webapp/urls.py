from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('register/', views.register_user, name='register_user'),
    path('record/<int:pk>', views.customer_record, name='c_record'),
    path('delete_record/<int:pk>', views.delete_record, name='d_record'),
]
