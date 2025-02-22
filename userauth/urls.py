from django.urls import path
from userauth.views import *

urlpatterns = [
    path("signup/",signup),
    path("login/",login_user),
    path("business_signup/",business_signup)
]