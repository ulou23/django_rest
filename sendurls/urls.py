from django.urls import path
from sendurls import views


app_name='sendurls'

urlpatterns = [
    path('', views.UrlinputList.as_view(),name='urllist'),
    path('/<int:pk>/',views.UrlDetail.as_view()),
]
