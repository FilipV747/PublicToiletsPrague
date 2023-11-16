from django.urls import path
from prague import views

app_name = 'prague'

urlpatterns = [
    path('', views.index, name='index'),
    path('toilets', views.toilet_list, name='toilets'),
    path('toilets/free', views.free_toilets, name='free_toilets'),
    path('toilets/<slug:slug>/', views.toilet_detail, name='toilet_detail'),
]