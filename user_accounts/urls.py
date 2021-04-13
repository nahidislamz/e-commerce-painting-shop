from django.urls import path
from .views import *

urlpatterns = [
    path('signin/', signInPage, name='signin'),
    path('logout/', logoutPage, name='logout'),
    path('signup/', signUpPage, name='signup'),
    path('profile/', profilePage, name="profile"),

]
