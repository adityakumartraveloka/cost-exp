from django.urls import path
from . import views

urlpatterns = [
    # path("", views.registeraccessrequestview, name='register'),/
    path("",views.registeracessrequest, name='wnasdf')
    # path("", views.RegisterAccessResquestView.as_view(), name='register'),
    # path('<int:id>/', views.registeracessrequestupdate, name='register-update')
]
