from django.urls import path
from . import views
urlpatterns= [
    path("profile/", views.profile, name="profile"),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('subscribe/<str:subscription_type>/', views.subscribe, name='subscribe'),
    path('join/', views.join, name="join"),
    path('subscription-redirect/', views.redirect, name= "subscription_redirect")
]