from django.urls import path
from . import views

urlpatterns = [
    path("", views.registeraccessrequest, name='register'),
    path("<int:id>", views.registeraccessrequestupdate, name='register-update')
]
