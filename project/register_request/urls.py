from django.urls import path
from . import views

urlpatterns = [
    path("", views.registeraccessrequest, name='register'),
    path("<int:id>", views.registeraccessrequestupdate, name='register-update'),
    path("approve", views.approverequest, name='approve-request'),
    path("approve/<int:id>", views.approverequestupdate, name='approve-request'),

]
