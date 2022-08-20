from django.urls import path
from . import views
urlpatterns =[
  path('',views.post_list, name='post_list'),
  path('<int:year>/',views.get_months, name='get_months'),
  path('hot_100/<str:month>/', views.get_hot_100,name='get_hot_100'), 
  path('current_100/',views.get_current_100,name='current_100'),
  path('track/<str:track>/<str:artist>', views.get_url, name='preview_url')
]