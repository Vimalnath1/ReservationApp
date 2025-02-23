from django.urls import path
from userauth.views import *

urlpatterns = [
    path("signup/",signup),
    path("login/",login_user),
    path("business_signup/",business_signup),
    path('api/fetch_user_id/', fetch_user_id,name="fetch_user_id"),
    path('api/get_queue/', get_queue,name="get_queue"),
    path("make_customer/",make_customer),
    path('confirm/<int:booking_id>/', confirm_booking, name='confirm_booking'),
    path('show_places/',show_places),
    path("submit_data/",submit_data),
    path("calculate/",calculate),
    path("select_restaurant/",select_restaurant)
]