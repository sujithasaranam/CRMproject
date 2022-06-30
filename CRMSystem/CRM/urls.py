from .views import RegisterAPI,EnquiryAPI
from django.urls import path
from . import views


urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/enquiry/', EnquiryAPI.as_view(), name='enquiry'),
    path('api/login/', views.login, name='login'),
    path('api/home',views.home,name="home"),
    path('api/hide',views.hide,name="hide"),
]
