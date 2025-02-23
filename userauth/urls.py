from django.urls import path
from userauth.views import *

urlpatterns = [
    path("signup/",signup),
    path("login/",login_user),
    path("business_signup/",business_signup),
    path('api/fetch_user_id/', fetch_user_id,name="fetch_user_id"),
    path('api/get_queue/', get_queue,name="get_queue"),
    path("make_customer/",make_customer)
]