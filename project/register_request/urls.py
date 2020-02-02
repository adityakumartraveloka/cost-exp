from django.urls import path
from . import views

urlpatterns = [
    path("", views.registeracessrequest, name='register'),
    path('<int:id>/', views.registeracessrequestupdate, name='register-update')
]
