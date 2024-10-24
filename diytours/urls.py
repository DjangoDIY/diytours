## add app urls here

from django.urls import path
from . import views

urlpatterns = [
    path("onsale",views.tour_promo, name="tour_promo"),
    path("",views.tour_index, name="tour_index"),
    path("<str:title>", views.tour_detail, name="tour_detail"),
    path("category/<str:category>", views.tour_category, name="tour_category"),
    path("location/<str:location>", views.tour_location, name="tour_location" ),
    path("tag/<str:tag>", views.tour_tag, name= "tour_tag"),
    path("activity/<str:activity>", views.tour_activity, name="tour_activity"),


]