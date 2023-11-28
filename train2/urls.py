from django.urls import path
from . import views

urlpatterns = [
    path("", views.booking, name = "status"),
    path("status", views.status, name = "status"),
    path("booking", views.booking, name = "booking"),
    path("search_by_name", views.search_by_name, name = "search_by_name"),
    path("search_by_station", views.search_by_station, name = "search_by_station"),
    path("contactus", views.contact_us, name = "contactus"),
    path("search_train", views.search_train, name = "search_by_name"),
    path("search_status", views.search_status, name = "search_status"),
    path("search_station", views.search_station, name = "search_station"),
    path("login", views.loginUser, name = "login"),
    path("signup", views.signupUser, name = "signup"),
    path("logout", views.logoutUser, name = "logout"),
    path("send_otp", views.send_otp, name = "send_otp"),
    path("verify_otp", views.verify_otp, name = "verify_otp"),
    path("forgot_password", views.forgot_password, name = "forgot_password"),
    path("search_booking", views.search_booking, name = "search_booking"),

]