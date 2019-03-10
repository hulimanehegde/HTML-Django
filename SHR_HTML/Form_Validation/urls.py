from django.contrib import admin
from django.urls import path

from Form_Validation import views

urlpatterns = {

    path('recivedata', views.createpost, name="createpost")
}
